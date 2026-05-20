import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="TikTok Downloader Pro")
st.title("TikTok Video Downloader")

url = st.text_input("Enter TikTok URL here")

if url:
    if st.button("Download Now"):
        with st.spinner('Downloading... please wait.'):
            try:
                # TikTok ke liye best stream ka path force karna
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': 'video.mp4',
                    'noplaylist': True,
                    'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                if os.path.exists('video.mp4'):
                    # Video play karein
                    st.video('video.mp4')
                    
                    # File save karne ka option
                    with open('video.mp4', "rb") as file:
                        st.download_button(
                            label="⬇️ Save to Gallery",
                            data=file,
                            file_name="tiktok_video.mp4",
                            mime="video/mp4"
                        )
                    st.success("Download mukammal hua!")
            except Exception as e:
                st.error(f"Error: {e}")
                st.info("Agar video nahi chal rahi, toh iska matlab server par video stream support nahi hai.")
