import streamlit as st
import requests

# Page layout setup
st.set_page_config(page_title="TikTok Downloader Pro", layout="centered")

st.title("TikTok Downloader Pro")

# 1. URL Input
url = st.text_input("Enter TikTok URL here:")

# Session state to keep video data
if "video_data" not in st.session_state:
    st.session_state.video_data = None

# 2. Fetch Button
if st.button("Fetch Video Details"):
    if url:
        with st.spinner('Fetching...'):
            try:
                api = f"https://www.tikwm.com/api/?url={url}"
                res = requests.get(api).json()
                if res.get('code') == 0:
                    st.session_state.video_data = res['data']
                    st.success("Details fetched! Now select quality.")
                else:
                    st.error("Invalid URL or video not found.")
            except:
                st.error("Error connecting to server.")

# 3. Show options only if data is fetched
if st.session_state.video_data:
    data = st.session_state.video_data
    
    # Quality selection
    quality = st.radio("Select Video Quality:", ("Normal", "HD (High)"), horizontal=True)
    video_url = data.get('hdplay') if quality == "HD (High)" else data.get('play')
    
    # Video preview
    st.video(video_url)
    
    # Save button
    st.markdown(f'<a href="{video_url}" target="_blank" style="display: block; text-align: center; background: #28a745; color: white; padding: 15px; border-radius: 10px; text-decoration: none; font-weight: bold; font-size: 18px;">⬇️ Save to Gallery</a>', unsafe_allow_html=True)
