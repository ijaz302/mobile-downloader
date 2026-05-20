import streamlit as st
import requests

# Page layout setup for mobile
st.set_page_config(page_title="TikTok Pro Downloader", layout="centered")

# Custom CSS for better mobile experience
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; background-color: #ff4b4b; color: white; }
    .download-btn { display: block; text-align: center; background: #28a745; color: white; 
                    padding: 15px; border-radius: 10px; text-decoration: none; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("TikTok Downloader Pro")

url = st.text_input("Enter TikTok URL here:")

if url:
    with st.spinner('Fetching details...'):
        try:
            # Using tikwm API for high quality and watermark-free
            api = f"https://www.tikwm.com/api/?url={url}"
            res = requests.get(api).json()
            
            if res.get('code') == 0:
                data = res['data']
                
                # Quality selection for mobile
                quality = st.radio("Select Video Quality:", ("Normal", "HD (High)"), horizontal=True)
                
                # Selecting correct URL based on quality
                video_url = data.get('hdplay') if quality == "HD (High)" else data.get('play')
                
                # Video Preview
                st.video(video_url)
                
                # Download/Save Button
                st.markdown(f'<a href="{video_url}" target="_blank" class="download-btn">⬇️ Download / Save to Gallery</a>', unsafe_allow_html=True)
            else:
                st.error("Invalid URL or video not found.")
        except Exception as e:
            st.error("Network error. Please try again.")
