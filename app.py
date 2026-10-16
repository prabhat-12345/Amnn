import streamlit as st

st.set_page_config(page_title="Happy Birthday Aman!", page_icon="🎉")

# Balloons animation automatically chalega jab page load hoga
st.balloons()

# Custom CSS bade text ke liye
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #FFE5EC 0%, #FFB3C6 100%);
    }
    .birthday-text {
        font-family: 'Arial Black', sans-serif;
        font-size: 70px;
        color: #FF4757;
        text-align: center;
        text-shadow: 3px 3px 0px #FFFFFF;
        padding-top: 50px;
    }
    .name-text {
        font-family: 'Arial Black', sans-serif;
        font-size: 100px;
        color: #2ED573;
        text-align: center;
        text-shadow: 4px 4px 0px #FFFFFF;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="birthday-text">🎉 HAPPY BIRTHDAY 🎉</div>', unsafe_allow_html=True)
st.markdown('<div class="name-text">AMAN</div>', unsafe_allow_html=True)
