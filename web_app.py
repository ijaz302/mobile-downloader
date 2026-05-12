import streamlit as st
import yt_dlp
import os

SAVE_PATH = os.getcwd()

st.set_page_config(page_title="Mobile Downloader Pro", page_icon="📱")
st.title("📱 Universal Mobile Downloader")

url = st.text_input("Paste Video Link Here:")
quality = st.selectbox("Select Video Quality:", ["Best (High)", "720p", "480p"])

if st.button("DOWNLOAD NOW"):
    if url:
        try:
            st.info(f"🔄 Processing {quality} video... This may take a minute.")
            
            # Universal Settings for TikTok & Instagram
            opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': os.path.join(SAVE_PATH, 'downloaded_video.mp4'),
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }],
                'ffmpeg_location': '/usr/bin/ffmpeg',
                'merge_output_format': 'mp4',
                
                # --- NEW SECURITY BYPASS ---
                'nocheckcertificate': True,
                'no_warnings': True,
                'quiet': True,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'referer': 'https://www.tiktok.com/',
                'add_header': [
                    'Accept-Language: en-US,en;q=0.9',
                    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                ],
            }
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
            
            st.success("✅ Download Complete!")
            
            with open("downloaded_video.mp4", "rb") as file:
                st.download_button(
                    label="📥 SAVE TO GALLERY / MOBILE",
                    data=file,
                    file_name="my_video.mp4",
                    mime="video/mp4"
                )
            st.balloons()
            
        except Exception as e:
            st.error("Error: TikTok/Instagram security blocked the request. Please try again or update yt-dlp.")
