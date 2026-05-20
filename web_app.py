import streamlit as st
import requests

st.set_page_config(page_title="TikTok Downloader Pro", layout="centered")
st.title("TikTok Video Downloader")

url = st.text_input("Enter TikTok URL here")

if url:
    if st.button("Download Now"):
        with st.spinner('Fetching Video...'):
            try:
                # TikTok Downloader API (No Watermark)
                api = f"https://www.tikwm.com/api/?url={url}"
                res = requests.get(api).json()
                
                if res.get('code') == 0:
                    video_data = res['data']
                    video_url = video_data['play'] # Direct video URL
                    
                    st.success("Video mil gayi!")
                    st.video(video_url)
                    
                    # Direct link for gallery save
                    st.markdown(f'<a href="{video_url}" target="_blank" style="display: block; text-align: center; background: #ff4b4b; color: white; padding: 15px; border-radius: 10px; text-decoration: none; font-weight: bold;">⬇️ Save Video to Gallery</a>', unsafe_allow_html=True)
                else:
                    st.error("Video nahi mil saki. Link check karein.")
            except Exception as e:
                st.error(f"Error: {e}")
