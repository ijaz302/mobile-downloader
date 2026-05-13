import streamlit as st
import yt_dlp
import os
import time  # Ye zaroori hai videos mix hone se bachane ke liye

st.set_page_config(page_title="Universal Downloader", page_icon="📲")
st.title("📲 Universal Mobile Downloader")

url = st.text_input("Paste Video Link Here:", placeholder="https://...")

if st.button("DOWNLOAD NOW"):
    if url:
        try:
            with st.spinner("Processing..."):
                # Har baar naya naam banane ke liye time use kiya hai
                unique_name = f"video_{int(time.time())}.mp4"
                
                ydl_opts = {
                    'format': 'best',
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                    'outtmpl': unique_name,
                    'quiet': True
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                # Video display aur download button
                with open(unique_name, "rb") as f:
                    video_bytes = f.read()
                    st.video(video_bytes)
                    st.download_button("Save to Device", video_bytes, file_name=unique_name)
                
                # Kaam khatam hone ke baad file delete kar dein
                os.remove(unique_name)
                
        except Exception as e:
            st.error("Security Block! Please try again after some time or update yt-dlp.")
    else:
        st.warning("Pehle link paste karein!")
