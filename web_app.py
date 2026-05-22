import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="TikTok Downloader Pro", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; background-color: #ff4b4b; color: white; font-weight: bold; }
    .download-btn { display: block; text-align: center; background: #28a745; color: white; 
                    padding: 15px; border-radius: 10px; text-decoration: none; font-weight: bold; margin-top: 10px; }
    .footer { text-align: center; margin-top: 50px; font-size: 12px; color: #888; }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("🚀 TikTok Downloader Pro")
st.subheader("Fast & Watermark-Free")

# URL Input
url = st.text_input("Paste your TikTok URL here:")

if "video_data" not in st.session_state:
    st.session_state.video_data = None

# Fetch Logic
if st.button("Fetch & Download"):
    if url:
        with st.spinner('Fetching video details...'):
            try:
                api = f"https://www.tikwm.com/api/?url={url}"
                res = requests.get(api).json()
                if res.get('code') == 0:
                    st.session_state.video_data = res['data']
                else:
                    st.error("Invalid URL or Video not found.")
            except:
                st.error("Error connecting to server. Try again.")

# Display Results
if st.session_state.video_data:
    data = st.session_state.video_data
    
    # Quality Selection
    quality = st.radio("Select Video Quality:", ("Normal", "HD (High)"), horizontal=True)
    video_url = data.get('hdplay') if quality == "HD (High)" else data.get('play')
    
    # Preview
    st.video(video_url)
    
    # Download Button
    st.markdown(f'<a href="{video_url}" target="_blank" class="download-btn">⬇️ Save to Gallery</a>', unsafe_allow_html=True)
    
    st.info("Tip: If the video plays instead of downloading, long-press on it and select 'Save Video'.")

# Footer
st.markdown("---")
st.markdown("""
    <div class="footer">
        <p>© 2026 TikTok Downloader Pro | All Rights Reserved</p>
        <p>Disclaimer: This tool is not affiliated with TikTok.</p>
    </div>
""", unsafe_allow_html=True)
