import streamlit as st
import requests

# Layout: Wide aur clean
st.set_page_config(page_title="TikTok Downloader", layout="wide")

# CSS: Professional Purple/Modern Styling
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .main-box {
        background-color: #7b2cbf;
        padding: 40px;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.2);
    }
    .stTextInput > div > div > input {
        padding: 20px;
        border-radius: 10px;
        border: none;
    }
    .stButton > button {
        background-color: #3c096c;
        color: white;
        width: 100%;
        padding: 15px;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Main Header Box
st.markdown("<div class='main-box'>", unsafe_allow_html=True)
st.title("🎬 TikTok Video Downloader")
st.write("Download TikTok videos in HD, without watermark.")

url = st.text_input("", placeholder="Paste TikTok link here...")
if st.button("Download"):
    if url:
        with st.spinner('Fetching...'):
            api = f"https://www.tikwm.com/api/?url={url}"
            res = requests.get(api).json()
            if res.get('code') == 0:
                st.video(res['data']['play'])
            else:
                st.error("Invalid link!")
st.markdown("</div>", unsafe_allow_html=True)

# FAQ Section (Jaisa video mein tha)
st.write("---")
st.header("Frequently Asked Questions")
with st.expander("How to download TikTok video without watermark?"):
    st.write("1. Copy the video link from TikTok app. 2. Paste it in the box above. 3. Click Download.")
with st.expander("Is this tool free?"):
    st.write("Yes, our downloader is 100% free and unlimited.")
with st.expander("Does it work on mobile?"):
    st.write("Yes, it works perfectly on all mobile browsers.")
