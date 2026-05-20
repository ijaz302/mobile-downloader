import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="TikTok Downloader")
st.title("TikTok Video Downloader")

url = st.text_input("Enter TikTok URL here")

if url:
    if st.button("Download Now"):
        st.write("Processing... please wait.")
        try:
            # TikTok ke liye format 'best' hi rakhein, ye bina merge kiye download karega
            ydl_opts = {
                'format': 'best',
                'outtmpl': 'tiktok_video.mp4',
                'noplaylist': True,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            if os.path.exists('tiktok_video.mp4'):
                with open('tiktok_video.mp4', "rb") as file:
                    st.download_button(
                        label="Download Full Video",
                        data=file,
                        file_name="tiktok_video.mp4",
                        mime="video/mp4"
                    )
                st.success("Video ready to download!")
                
        except Exception as e:
            st.error(f"Error: {e}")
