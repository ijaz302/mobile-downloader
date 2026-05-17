import streamlit as st
import yt_dlp
import os
import time

st.set_page_config(page_title="Universal Downloader", page_icon="📲", layout="centered")

st.title("📲 Universal Mobile Downloader")
st.write("TikTok, Instagram, aur YouTube videos download karein.")

url = st.text_input("Paste Video Link Here:", placeholder="https://...")

if st.button("DOWNLOAD NOW"):
    if url:
        try:
            with st.spinner("Processing... Request ko bypass kiya ja raha hai."):
                
                timestamp = int(time.time())
                unique_filename = f"video_{timestamp}.mp4"
                
                ydl_opts = {
                    'format': 'best[ext=mp4]/best',
                    'outtmpl': unique_filename,
                    'quiet': True,
                    'no_warnings': True,
                    
                    # Fake mobile browser details taake platform block na kare
                    'user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                    'geo_bypass': True,
                    'http_headers': {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.9',
                    }
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
                    st.error("Video file generate nahi ho saki. Link check karein.")

        except Exception as e:
            st.error("Server Temporary Blocked! Instagram ne free server ka connection rok diya hai. Kuch dair baad koi doosra link try karein.")
    else:
        st.warning("Pehle koi link paste karein!")
