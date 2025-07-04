import streamlit as st
import base64
import os

def set_background(image_file: str):
    abs_path = os.path.join(os.path.dirname(__file__), image_file)
    
    if not os.path.exists(abs_path):
        st.warning(f"⚠️ Background image '{image_file}' not found. Skipping background setup.")
        return

    with open(abs_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def custom_success(msg, width="60%"):
    st.markdown(f"""
        <div style='
            background-color: #e0ffe0;
            padding: 10px 20px;
            border-left: 5px solid #33cc33;
            border-radius: 5px;
            color: #006600;
            width: {width};
            margin: 10px auto;
            font-size: 16px;
        '>
             {msg}
        </div>
    """, unsafe_allow_html=True)

def custom_warning(msg, width="60%"):
    st.markdown(f"""
        <div style='
            background-color: #fff8e1;
            padding: 10px 20px;
            border-left: 5px solid #ff9800;
            border-radius: 5px;
            color: #e65100;
            width: {width};
            margin: 10px auto;
            font-size: 16px;
        '>
            ⚠️ {msg}
        </div>
    """, unsafe_allow_html=True)

def custom_info(msg, width="60%"):
    st.markdown(f"""
        <div style='
            background-color: #e3f2fd;
            padding: 10px 20px;
            border-left: 5px solid #2196f3;
            border-radius: 5px;
            color: #0d47a1;
            width: {width};
            margin: 10px auto;
            font-size: 16px;
        '>
            ℹ️ {msg}
        </div>
    """, unsafe_allow_html=True)

# 🔹 Apply styles to selectbox, textarea and buttons for better UX
def apply_custom_styles():
    st.markdown("""
        <style>
        /* Customize selectbox label */
        .stSelectbox label {
            color: white !important;
            font-weight: bold;
            font-size: 16px;
        }

        /* Customize text area label */
        .stTextArea label {
            color: white !important;
            font-weight: bold;
            font-size: 16px;
        }

        /* Style the input box & text area */
        .stSelectbox div[data-baseweb="select"],
        .stTextArea textarea {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: black !important;
            border-radius: 10px;
            border: 1px solid white;
        }

        /* Customize buttons */
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 10px;
        }

        .stButton > button:hover {
            background-color: #45a049;
        }
        </style>
    """, unsafe_allow_html=True)


