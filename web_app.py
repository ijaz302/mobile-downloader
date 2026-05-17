import streamlit as st
import yt_dlp
import os
import time

# Page Configuration
st.set_page_config(page_title="Universal Downloader", page_icon="📲", layout="centered")

st.title("📲 Universal Mobile Downloader")
st.write("TikTok, Instagram, aur YouTube videos download karein.")

# 1. QUALITY SELECTION DROPDOWN
quality_choice = st.selectbox(
    "⚙️ Select Video Quality:",
    ["Best Quality (HD/1080p)", "Normal Quality (SD/720p)", "Low Data Mode (360p)"]
)

url = st.text_input("Paste Video Link Here:", placeholder="https://...")

if st.button("DOWNLOAD NOW"):
    if url:
        try:
            with st.spinner("🚀 Server line bypass ki ja rahi hai... Please wait."):
                timestamp = int(time.time())
                unique_filename = f"video_{timestamp}.mp4"
                
                # Dynamic format selection based on user choice
                format_opt = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
                if "Normal" in quality_choice:
                    format_opt = 'worstvideo[height>=720]+bestaudio/best'
                elif "Low" in quality_choice:
                    format_opt = 'worst[ext=mp4]/worst'

                # Core Engine Settings (Bypassing blocks)
                ydl_opts = {
                    'format': format_opt,
                    'outtmpl': unique_filename,
                    'quiet': True,
                    'no_warnings': True,
                    'geo_bypass': True,
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                }

                # Executing download
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                # Reading file and sending to user interface
                if os.path.exists(unique_filename):
                    with open(unique_filename, "rb") as f:
                        video_bytes = f.read()
                    
                    st.success("✨ Video successfully fetched!")
                    st.write(f"🎯 Download Quality: **{quality_choice}**")
                    
                    # Video Player Display
                    st.video(video_bytes)
                    
                    # 2. SAVE TO GALLERY BUTTON
                    st.download_button(
                        label="📥 Save to Device / Gallery",
                        data=video_bytes,
                        file_name=f"download_{timestamp}.mp4",
                        mime="video/mp4"
                    )
                    
                    # Clean up space
                    os.remove(unique_filename)
                else:
                    st.error("Server connection timeout. Ek baar dobara DOWNLOAD NOW par click karein.")

        except Exception as e:
            st.error("Video temporarily restricted by platform security. Please try another video link.")
    else:
        st.warning("Pehle koi link paste karein!")