import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Pro TikTok Downloader")
st.title("TikTok Downloader Pro")

url = st.text_input("Enter TikTok URL here")

if url:
    try:
        with st.spinner('Fetching Video...'):
            ydl_opts = {'format': 'best', 'outtmpl': 'temp_video.mp4'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            # Video display karein taake aap check kar sakein
            if os.path.exists('temp_video.mp4'):
                st.video('temp_video.mp4')
                st.success("Video load ho gayi! Ab niche se save karein.")
                
                # Save to Gallery/Device Option
                with open('temp_video.mp4', "rb") as file:
                    st.download_button(
                        label="⬇️ Save to Gallery / Download",
                        data=file,
                        file_name="tiktok_video.mp4",
                        mime="video/mp4"
                    )
                    
    except Exception as e:
        st.error(f"Error: {e}")
