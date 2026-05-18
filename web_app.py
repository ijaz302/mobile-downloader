import streamlit as st
import yt_dlp
import requests
import urllib.parse
import random
import time
import re
import os

# Fake user-agents for bypassing security alerts
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1"
]

# Browser Tab Configuration
st.set_page_config(
    page_title="YouTube Video Downloader",
    page_icon="🔻",
    layout="centered"
)

# Main Headings
st.title("🔻 YouTube Video Downloader")
st.markdown("### Free. No signup. Download now.")

# User Input Widgets
quality = st.selectbox("⚙️ Select Video Quality:", ["720p (High)", "360p (Standard)"])
video_url = st.text_input("Paste Video Link Here:", placeholder="https://www.youtube.com/watch?v=...")

# URL filter function
def clean_youtube_url(input_text):
    url_match = re.search(r'(https?://(?:www\.)?(?:youtube\.com|youtu\.be)/[^\s]+)', input_text)
    if url_match:
        return url_match.group(0)
    return input_text

# Secure download logic
def try_direct_download(url, quality_choice):
    try:
        clean_url = clean_youtube_url(url)
        time.sleep(random.uniform(1.0, 2.5))
        
        format_setting = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]'
        if quality_choice == "360p (Standard)":
            format_setting = 'worstvideo[ext=mp4]+worstaudio[ext=m4a]/worst[ext=mp4]'

        ydl_opts = {
            'format': format_setting,
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'http_headers': {'User-Agent': random.choice(USER_AGENTS)},
            'quiet': True,
            'no_warnings': True,
        }
        
        cookies_file = "cookies.txt"
        if os.path.exists(cookies_file) and os.path.getsize(cookies_file) > 0:
            ydl_opts['cookiefile'] = cookies_file

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(clean_url, download=True)
            video_filename = ydl.prepare_filename(info_dict)
            video_title = info_dict.get('title', 'YouTube_Video')
            
            with open(video_filename, 'rb') as f:
                video_bytes = f.read()
                
            os.remove(video_filename)
            return True, video_bytes, video_title

    except Exception as e:
        error_msg = str(e)
        if "403" in error_msg or "Sign in" in error_msg:
            return False, None, "Google Security Alert: Please update your cookies.txt file on GitHub."
        return False, None, f"Request handled smoothly. (Error: {error_msg})"

# Download Button
if st.button("📥 Download"):
    if video_url:
        with st.spinner("Bypassing security and fetching video... Please wait..."):
            success, result_data, details = try_direct_download(video_url, quality)
            
            if success:
                st.success(f"✨ '{details}' successfully processed!")
                st.download_button(
                    label="💾 Click Here to Save Video",
                    data=result_data,
                    file_name=f"{details}.mp4",
                    mime="video/mp4"
                )
            else:
                st.error(details)
    else:
        st.warning("Pehle koi link toh paste karein!")

# Footer for SEO
st.write("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📥 Best YouTube Downloader")
    st.write("Our tool helps you download high-quality YouTube videos and Shorts instantly without any registration or signup.")

with col2:
    st.markdown("### ❓ Frequently Asked Questions")
    with st.expander("Is this downloader free to use?"):
        st.write("Yes, this tool is 100% free and requires no registration.")
    with st.expander("Does it support mobile devices?"):
        st.write("Absolutely! This app is fully optimized for mobile devices, tablets, and Chromebooks.")
