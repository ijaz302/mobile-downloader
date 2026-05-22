import streamlit as st
import requests

st.set_page_config(page_title="TikTok Downloader Pro", layout="centered")

st.title("🚀 TikTok Downloader Pro")

url = st.text_input("Paste TikTok link here:")

if "video_data" not in st.session_state:
    st.session_state.video_data = None

if st.button("Fetch & Download"):
    if url:
        with st.spinner('Fetching...'):
            try:
                # TikTok API call
                api = f"https://www.tikwm.com/api/?url={url}"
                res = requests.get(api).json()
                if res.get('code') == 0:
                    st.session_state.video_data = res['data']
                else:
                    st.error("Invalid URL or Video restricted.")
            except:
                st.error("Error connecting to server.")

if st.session_state.video_data:
    data = st.session_state.video_data
    
    # Hum 'play' link use karenge jo jyada stable hai
    video_url = data.get('play')
    
    st.video(video_url)
    
    # Download button (Direct link)
    st.markdown(f'<a href="{video_url}" target="_blank" style="display: block; text-align: center; background: #007bff; color: white; padding: 15px; border-radius: 10px; text-decoration: none; font-weight: bold;">Download Video (No Watermark)</a>', unsafe_allow_html=True)
    
    st.success("If video doesn't download, right-click (or long press) the button and select 'Save link as'.")
