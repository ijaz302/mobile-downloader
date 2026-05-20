import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="TikTok Downloader Pro")
st.title("TikTok Downloader Pro")

url = st.text_input("Enter TikTok URL here")

if url:
    try:
        with st.spinner('Fetching Video...'):
            # TikTok ke liye best option jo bina FFmpeg ke chal sake
            ydl_opts = {
                'format': 'best', 
                'outtmpl': 'temp_video.mp4',
                'noplaylist': True,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            # Agar file download ho gayi hai toh play karein
            if os.path.exists('temp_video.mp4'):
                st.video('temp_video.mp4')
                
                # Save button
                with open('temp_video.mp4', "rb") as file:
                    st.download_button(
                        label="⬇️ Save to Gallery / Download",
                        data=file,
                        file_name="tiktok_video.mp4",
                        mime="video/mp4"
                    )
                    
    except Exception as e:
        st.error(f"Error: {e}")
