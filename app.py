import streamlit as st

st.set_page_config(
    page_title="Happy Birthday Aman!", 
    page_icon="🎂",
    layout="wide"
)

# Sirf balloons rakhe hain, snowflakes hata diye taaki text saaf dikhe
st.balloons()

st.markdown(
    """
    <style>
    /* Pura padding aur scrollbar khatam karne ke liye */
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }
    
    #MainMenu, header, footer {visibility: hidden;}
    
    /* Pure screen ko handle karne ke liye viewport adjustments */
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

    /* Text ko mobile screen ke ekdum center me lane ke liye container */
    .center-wrapper {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 80vh; /* Pura vertical space use karega */
        text-align: center;
    }

    /* Mobile standard ke liye ekdum bada Happy Birthday text */
    .giant-birthday {
        font-family: 'Arial Black', sans-serif;
        font-size: 11vw; /* Isko aur bada kiya hai */
        font-weight: 900;
        color: #ffffff;
        text-transform: uppercase;
        letter-spacing: 2px;
        line-height: 1.2;
        margin: 0;
        text-shadow: 0 0 15px rgba(255,255,255,0.6), 0 4px 10px rgba(0,0,0,0.3);
    }

    /* Mobile ke liye sabse bada AMAN text */
    .giant-name {
        font-family: 'Arial Black', sans-serif;
        font-size: 20vw; /* Ekdum giant mobile size */
        font-weight: 900;
        background: linear-gradient(to right, #ffe259, #ffa751);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 5px;
        line-height: 1.1;
        margin-top: 30px;
        display: block;
        filter: drop-shadow(3px 5px 10px rgba(0,0,0,0.4));
        animation: float 2s ease-in-out infinite;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-15px); }
    }

    /* Desktop screen par aur bada dikhane ke liye media query */
    @media (min-width: 769px) {
        .giant-birthday { font-size: 6vw; }
        .giant-name { font-size: 10vw; }
    }
    </style>
    
    <div class="center-wrapper">
        <div class="giant-birthday">🎉 HAPPY<br>BIRTHDAY 🎉</div>
        <div class="giant-name">AMAN</div>
    </div>
    """, 
    unsafe_allow_html=True
)
