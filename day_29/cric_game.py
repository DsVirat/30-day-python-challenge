import random

# List of possible runs per ball
runs = [0, 1, 2, 3, 4, 6]

def play_ball():
    """
    Simulate one ball being played.
    
    Returns:
        run (int): Number of runs scored on that ball.
        is_out (bool): True if the ball resulted in an "out" (i.e. run == 0), otherwise False.
    """
    run = random.choice(runs)
    is_out = (run == 0)
    return run, is_out

def get_toss_winner(player1, player2):
    """
    Randomly select and return the toss winner from two players.
    """
    return random.choice([player1, player2])

def check_target_met(score, target):
    """
    Check if the provided score has met or exceeded the target.
    
    Returns:
        bool: True if score > target, False otherwise.
    """
    return score > target

def determine_winner(score1, score2, player1, player2):
    """
    Determine the match winner based on both innings’ scores.
    
    Args:
        score1 (int): Score of the first batting team.
        score2 (int): Score of the second batting team.
        player1 (str): Name of the first batting team.
        player2 (str): Name of the second batting team.
    
    Returns:
        str: A message declaring the winner or if it's a draw.
    """
    if score1 > score2:
        return f"{player1} wins the match by {score1 - score2} run(s)!"
    elif score2 > score1:
        return f"{player2} wins the match by successfully chasing down the target!"
    else:
        return "It's a draw!"
