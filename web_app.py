import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="TikTok Downloader", layout="centered")

# Custom Styling (Professional Look)
st.markdown("""
    <style>
    .main-title { text-align: center; color: #ff4b4b; }
    .stTextInput>div>div>input { border: 2px solid #ff4b4b; border-radius: 10px; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #ff4b4b; color: white; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🚀 TikTok Video Downloader</h1>", unsafe_allow_html=True)
st.write("---")

# Input Section
url = st.text_input("Paste TikTok link here:", placeholder="https://www.tiktok.com/@username/video/...")

if st.button("Download Now"):
    if url:
        with st.spinner('Fetching video...'):
            try:
                # Using tikwm API
                api = f"https://www.tikwm.com/api/?url={url}"
                res = requests.get(api).json()
                
                if res.get('code') == 0:
                    data = res['data']
                    st.success("Video found!")
                    st.video(data.get('play'))
                    st.markdown(f'<a href="{data.get("play")}" target="_blank" style="display:block; text-align:center; background:#28a745; color:white; padding:10px; border-radius:10px; text-decoration:none;">⬇️ Click to Download</a>', unsafe_allow_html=True)
                else:
                    st.error("Could not fetch video. Please check the URL.")
            except Exception as e:
                st.error("Server error. Please try again later.")

# --- FAQ Section (As per your screen recording) ---
st.write("---")
st.subheader("Frequently Asked Questions")
with st.expander("How to download TikTok video without watermark?"):
    st.write("Just copy the link from TikTok, paste it in the box above, and click Download.")
with st.expander("Is this tool free?"):
    st.write("Yes, this tool is 100% free and unlimited.")
with st.expander("Does it work on mobile?"):
    st.write("Yes, it works perfectly on iPhone and Android browsers.")
