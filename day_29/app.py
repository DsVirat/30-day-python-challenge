import streamlit as st
from cric_game import play_ball, get_toss_winner, check_target_met, determine_winner
from ui_utils import set_background, custom_success, custom_warning, custom_info

set_background("bg.png")

# Initialize session state to manage the game flow
if 'game_stage' not in st.session_state:
    st.session_state.update({
        'game_stage': 0,         # 0: Enter Names, 1: Toss, 2: Innings, 3: Summary
        'player_1': '',
        'player_2': '',
        'toss_winner': '',
        'choice': '',
        'batting_first': '',
        'batting_second': '',
        'run1': 0,
        'run2': 0,
        'innings': 1,
        'target': None,
        'out': False,
        'game_over': False,
        'current_player': '',
    })

st.title("🏏DuoCrik")

# ---------------------------
# 🔹 Stage 0: Player Name Input
# ---------------------------
if st.session_state.game_stage == 0:
    st.header("Enter Player Names")
    player1 = st.text_input("Player 1 Name")
    player2 = st.text_input("Player 2 Name")

    if st.button("Start Match") and player1 and player2:
        st.session_state.player_1 = player1.strip().capitalize()
        st.session_state.player_2 = player2.strip().capitalize()
        st.session_state.game_stage = 1
        st.rerun()

# ---------------------------
# 🔹 Stage 1: Toss + Bat/Bowl Choice
# ---------------------------
elif st.session_state.game_stage == 1:
    st.header("🪙 Toss Time")

    if not st.session_state.toss_winner:
        st.session_state.toss_winner = get_toss_winner(st.session_state.player_1, st.session_state.player_2)

    custom_success(f"{st.session_state.toss_winner} won the toss!")

    choice = st.radio(f"What will {st.session_state.toss_winner} choose?", ["Bat", "Bowl"])

    if st.button("Confirm Choice"):
        st.session_state.choice = choice.lower()

        # Determine who bats first
        if st.session_state.toss_winner == st.session_state.player_1:
            st.session_state.batting_first = (
                st.session_state.player_1 if choice.lower() == 'bat' else st.session_state.player_2
            )
            st.session_state.batting_second = (
                st.session_state.player_2 if choice.lower() == 'bat' else st.session_state.player_1
            )
        else:
            st.session_state.batting_first = (
                st.session_state.player_2 if choice.lower() == 'bat' else st.session_state.player_1
            )
            st.session_state.batting_second = (
                st.session_state.player_1 if choice.lower() == 'bat' else st.session_state.player_2
            )

        st.session_state.current_player = st.session_state.batting_first
        st.session_state.game_stage = 2
        st.rerun()

# ---------------------------
# 🔹 Stage 2: Innings Play
# ---------------------------
elif st.session_state.game_stage == 2:
    st.subheader(f"Innings {st.session_state.innings}: {st.session_state.current_player} is batting")

    if not st.session_state.out and not st.session_state.game_over:
        if st.button("🏏 Play Ball"):
            run, is_out = play_ball()

            if is_out:
                custom_warning(f"💥 {st.session_state.current_player} got OUT!")
                st.session_state.out = True
            else:
                if st.session_state.innings == 1:
                    st.session_state.run1 += run
                    total = st.session_state.run1
                else:
                    st.session_state.run2 += run
                    total = st.session_state.run2
                    if check_target_met(total, st.session_state.run1):
                        st.session_state.game_over = True

                custom_success(f"🏏 {st.session_state.current_player} scored {run} run(s), Total: {total}")

    # Switch innings or end game
    if st.session_state.out or st.session_state.game_over:
        if st.session_state.innings == 1:
            st.session_state.target = st.session_state.run1 + 1
            st.session_state.innings = 2
            st.session_state.out = False
            st.session_state.current_player = st.session_state.batting_second
            custom_info(f"🎯 Target for {st.session_state.current_player}: {st.session_state.target}")
        else:
            st.session_state.game_over = True

        if st.button("Next"):
            st.rerun()

# ---------------------------
# 🔹 Stage 3: Match Summary
# ---------------------------
if st.session_state.game_over:
    st.header("📊 Match Summary")

    st.write(f"{st.session_state.batting_first}: {st.session_state.run1} runs")
    st.write(f"{st.session_state.batting_second}: {st.session_state.run2} runs")

    result = determine_winner(
        st.session_state.run1,
        st.session_state.run2,
        st.session_state.batting_first,
        st.session_state.batting_second
    )
    custom_success(result)

    # Centered play again button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Play Again"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
