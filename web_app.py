import streamlit as st
import requests

# Layout Config
st.set_page_config(page_title="TikTok Video Downloader", layout="wide")

# CSS Styling (Professional Look)
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stApp { max-width: 800px; margin: 0 auto; }
    .nav { text-align: center; padding: 10px; background: #fff; border-bottom: 2px solid #ddd; margin-bottom: 20px; }
    .download-box { background: #fff; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

# Navigation Bar
st.markdown("<div class='nav'>TikTok Downloader | Instagram Downloader | Twitter Downloader</div>", unsafe_allow_html=True)

# Main Title
st.title("🎬 TikTok Video Downloader")
st.write("---")

# Input Section with Container
with st.container():
    st.markdown("<div class='download-box'>", unsafe_allow_html=True)
    url = st.text_input("Paste TikTok link here:", placeholder="https://www.tiktok.com/...")
    if st.button("Download Now", use_container_width=True):
        if url:
            with st.spinner('Fetching...'):
                try:
                    api = f"https://www.tikwm.com/api/?url={url}"
                    res = requests.get(api).json()
                    if res.get('code') == 0:
                        st.video(res['data']['play'])
                        st.success("Success! You can watch your video below.")
                    else:
                        st.error("Invalid URL. Make sure it's a direct TikTok link.")
                except Exception as e:
                    st.error("Error connecting to server.")
    st.markdown("</div>", unsafe_allow_html=True)

# FAQ/Guide Section
st.write("## How to use")
st.info("1. Copy the video link from TikTok.\n2. Paste it in the box above.\n3. Click Download and wait for the preview.")

# Footer
st.markdown("<div style='text-align: center; margin-top: 50px; color: #888;'>© 2026 Professional Downloader Tool</div>", unsafe_allow_html=True)
