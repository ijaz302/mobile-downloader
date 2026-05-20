import streamlit as st
import yt_dlp
import os

# Page title
st.set_page_config(page_title="YouTube Downloader")
st.title("YouTube Downloader")

# Input field
url = st.text_input("Enter YouTube URL here")

# Download button
if st.button("Download"):
    if url:
        try:
            st.write("Downloading... please wait.")
            
            # yt-dlp options
            ydl_opts = {
                'format': 'best',
                'outtmpl': '%(title)s.%(ext)s',
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
            
            st.success(f"Downloaded successfully: {filename}")
            
            # File download button
            with open(filename, "rb") as file:
                st.download_button(
                    label="Click here to save the file",
                    data=file,
                    file_name=filename,
                    mime="video/mp4"
                )
                
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.error("Please provide a valid YouTube link.")
