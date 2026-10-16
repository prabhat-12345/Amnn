import streamlit as st

st.set_page_config(
    page_title="Happy Birthday Aman!", 
    page_icon="🎂",
    layout="wide" # Poori screen use karne ke liye wide layout
)

# Balloons aur snow effects
st.balloons()
st.snow()

st.markdown(
    """
    <style>
    /* Streamlit ki default top padding aur margin ko poora khatam karne ke liye */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    
    /* Header aur footer hide karne ke liye taaki sirf aapka text dikhe */
    #MainMenu, header, footer {visibility: hidden;}
    
    /* Poori screen par background animation fix karne ke liye */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientBG 10s ease infinite;
        position: fixed;
        width: 100vw;
        height: 100vh;
        top: 0;
        left: 0;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Pura full-screen container */
    .full-display-container {
        width: 100%;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    /* Ekdum Bada Happy Birthday Text */
    .giant-birthday {
        font-family: 'Arial Black', sans-serif;
        font-size: 8vw; /* Screen width ke hisab se automatic bada hoga */
        font-weight: 900;
        color: #ffffff;
        text-transform: uppercase;
        letter-spacing: 5px;
        line-height: 1;
        margin: 0;
        text-shadow: 0 0 20px #fff, 0 0 40px #ff4757, 0 0 60px #ff4757;
        animation: pulse 1.5s infinite alternate;
    }

    /* Sabse Bada AMAN Name Text */
    .giant-name {
        font-family: 'Arial Black', sans-serif;
        font-size: 14vw; /* Ekdum giant size */
        font-weight: 900;
        background: linear-gradient(to right, #ffe259, #ffa751);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 10px;
        line-height: 1.1;
        margin-top: 20px;
        display: block;
        filter: drop-shadow(5px 5px 15px rgba(0,0,0,0.4));
        animation: float 2.5s ease-in-out infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.05); }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }

    /* Mobile ke liye responsive scaling */
    @media (max-width: 768px) {
        .giant-birthday { font-size: 10vw; letter-spacing: 2px; }
        .giant-name { font-size: 18vw; letter-spacing: 4px; }
    }
    </style>
    
    <div class="full-display-container">
        <div class="giant-birthday">🎉 HAPPY BIRTHDAY 🎉</div>
        <div class="giant-name">AMAN</div>
    </div>
    """, 
    unsafe_allow_html=True
)
