import streamlit as st
import base64

# ✅ Background Image Function
def set_background(image_file: str):
    with open(image_file, "rb") as img_file:
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

# ✅ Custom Styled Message Boxes
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
            ✅ {msg}
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
