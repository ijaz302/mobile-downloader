import streamlit as st
import requests

# Layout: Wide aur clean
st.set_page_config(page_title="TikTok Downloader", layout="wide")

# CSS Styling: Professional Boxed Layout
st.markdown("""
    <style>
    /* Background Color */
    .stApp { background-color: #f0f2f6; }
    
    /* Center Box Styling */
    .main-box {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* Input Box styling */
    .stTextInput > div > div > input {
        border: 2px solid #ff4b4b;
        border-radius: 10px;
        padding: 15px;
    }
    
    /* Download Button */
    div.stButton > button {
        background-color: #ff4b4b;
        color: white;
        width: 100%;
        padding: 10px;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Layout: Columns ka use karke centering
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("<div class='main-box'>", unsafe_allow_html=True)
    st.title("🎬 TikTok Downloader")
    
    url = st.text_input("Paste TikTok link:", placeholder="https://www.tiktok.com/...")
    
    if st.button("Download Now"):
        if url:
            with st.spinner('Fetching...'):
                api = f"https://www.tikwm.com/api/?url={url}"
                res = requests.get(api).json()
                if res.get('code') == 0:
                    st.video(res['data']['play'])
                else:
                    st.error("Invalid URL")
    st.markdown("</div>", unsafe_allow_html=True)

    # How to section
    st.subheader("How to use")
    st.markdown("""
    <div style='background: white; padding: 20px; border-radius: 15px;'>
    1. Copy link from TikTok app.<br>
    2. Paste above and click Download.<br>
    3. Save video to your device.
    </div>
    """, unsafe_allow_html=True)
