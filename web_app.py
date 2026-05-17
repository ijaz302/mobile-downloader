import streamlit as st
import yt_dlp
import os
import time
import requests

st.set_page_config(page_title="Universal Downloader", page_icon="📲", layout="centered")

st.title("📲 Universal Mobile Downloader")
st.write("TikTok, Instagram, aur YouTube videos download karein.")

url = st.text_input("Paste Video Link Here:", placeholder="https://...")

if st.button("DOWNLOAD NOW"):
    if url:
        try:
            with st.spinner("Processing... Server security ko bypass kiya ja raha hai."):
                timestamp = int(time.time())
                unique_filename = f"video_{timestamp}.mp4"
                
                # Method 1: Agar link Instagram ka hai, to direct external API check karein
                if "instagram.com" in url:
                    # Public open-source API for Instagram content fetching
                    api_url = f"https://api.rest7.com/v1/instagram_video_downloader.php?url={url}"
                    response = requests.get(api_url, timeout=10)
                    if response.status_code == 200 and response.json().get('success'):
                        video_direct_url = response.json().get('file')
                        video_data = requests.get(video_direct_url).content
                        
                        st.video(video_data)
                        st.download_button(
                            label="📥 Save to Device / Gallery",
                            data=video_data,
                            file_name=f"instagram_{timestamp}.mp4",
                            mime="video/mp4"
                        )
                        st.stop()

                # Method 2: Standard Custom yt_dlp downloader (For YouTube, TikTok etc)
                ydl_opts = {
                    'format': 'best[ext=mp4]/best',
                    'outtmpl': unique_filename,
                    'quiet': True,
                    'no_warnings': True,
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'geo_bypass': True,
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                if os.path.exists(unique_filename):
                    with open(unique_filename, "rb") as f:
                        video_bytes = f.read()
                        st.video(video_bytes)
                        st.download_button(
                            label="📥 Save to Device / Gallery",
                            data=video_bytes,
                            file_name=f"download_{timestamp}.mp4",
                            mime="video/mp4"
                        )
                    os.remove(unique_filename)
                else:
                    st.error("Video file generate nahi ho saki. Link check karein ya thodi dair baad try karein.")

        except Exception as e:
            st.error("Server Timeout! Instagram free requests ko temporary block kar raha hai. Koi doosra link try karein.")
    else:
        st.warning("Pehle koi link paste karein!")
