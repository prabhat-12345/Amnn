import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Happy Birthday Aman! 🎂", 
    page_icon="👑",
    layout="centered"
)

# Balloons aur Confetti dono automatically chalyenge
st.balloons()
st.snow()  # Yeh premium falling effect dega

# Premium CSS Animations aur Custom UI
st.markdown(
    """
    <style>
    /* Premium Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Outer Wrapper for Card */
    .premium-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 40px 20px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
        margin-top: 50px;
        animation: fadeIn 2s ease-out;
    }

    /* Premium Neon Glow Text */
    .birthday-text {
        font-family: 'Poppins', 'Arial Black', sans-serif;
        font-size: 4.5rem;
        font-weight: 900;
        color: #ffffff;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin: 0;
        text-shadow: 0 0 10px #fff, 0 0 20px #ff4757, 0 0 30px #ff4757;
        animation: pulse 2s infinite alternate;
    }

    /* Premium Name Style with Gradient */
    .name-text {
        font-family: 'Poppins', 'Arial Black', sans-serif;
        font-size: 7rem;
        font-weight: 900;
        background: linear-gradient(to right, #ffe259, #ffa751);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 8px;
        margin-top: 10px;
        display: block;
        filter: drop-shadow(2px 4px 10px rgba(0,0,0,0.3));
        animation: float 3s ease-in-out infinite;
    }

    /* Animations definition */
    @keyframes fadeIn {
        from { opacity: 0; transform: scale(0.9); }
        to { opacity: 1; transform: scale(1); }
    }

    @keyframes pulse {
        0% { transform: scale(1); text-shadow: 0 0 10px #fff, 0 0 20px #ff4757, 0 0 30px #ff4757; }
        100% { transform: scale(1.02); text-shadow: 0 0 15px #fff, 0 0 30px #ff6b81, 0 0 45px #ff6b81; }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-15px); }
    }

    /* Mobile friendly fixes */
    @media (max-width: 600px) {
        .birthday-text { font-size: 2.2rem; }
        .name-text { font-size: 3.8rem; letter-spacing: 4px; }
        .premium-card { padding: 25px 10px; margin-top: 20px; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# UI render karna premium glass container me
st.markdown(
    """
    <div class="premium-card">
        <div class="birthday-text">✨ HAPPY BIRTHDAY ✨</div>
        <div class="name-text">AMAN</div>
    </div>
    """, 
    unsafe_allow_html=True
)
