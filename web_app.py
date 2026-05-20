import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="TikTok Downloader")
st.title("TikTok Video Downloader")

url = st.text_input("Enter TikTok URL here")

if url:
    try:
        # Fetch video details
        with st.spinner('Fetching video details...'):
            with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                info = ydl.extract_info(url, download=False)
                st.write(f"**Title:** {info.get('title')}")
                
        # Quality Selection
        quality_choice = st.selectbox("Select Quality", ["Best Quality", "Lower Quality"])
        format_str = 'best' if quality_choice == "Best Quality" else 'worst'

        if st.button("Download Now"):
            st.write("Downloading... please wait.")
            
            ydl_opts = {
                'format': format_str,
                'outtmpl': 'downloaded_video.mp4',
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            # File download button
            if os.path.exists('downloaded_video.mp4'):
                with open('downloaded_video.mp4', "rb") as file:
                    st.download_button(
                        label="Click to Save File",
                        data=file,
                        file_name="tiktok_video.mp4",
                        mime="video/mp4"
                    )
                st.success("Download ready!")
                
    except Exception as e:
        st.error(f"Error: {e}")
