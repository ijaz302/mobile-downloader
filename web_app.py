import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="YouTube Downloader")
st.title("YouTube Downloader")

# URL Input
url = st.text_input("Enter YouTube URL here")

# Check if cookies exist
cookies_path = 'cookies.txt'
if not os.path.exists(cookies_path):
    st.warning("Warning: cookies.txt file nahi mili. Download fail ho sakta hai.")

if url:
    try:
        # Definitive options for yt-dlp
        ydl_opts = {
            'format': 'best',
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'cookiefile': cookies_path if os.path.exists(cookies_path) else None,
            'quiet': True
        }
        
        with st.spinner('Fetching video details...'):
            with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                info = ydl.extract_info(url, download=False)
                st.success(f"Video found: {info.get('title')}")
                
        if st.button("Download Now"):
            st.write("Downloading... please wait.")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
            
            with open(filename, "rb") as file:
                st.download_button(
                    label="Click here to save the file",
                    data=file,
                    file_name=filename,
                    mime="video/mp4"
                )
                
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.info("Agar error 403 ya 'Sign in' ka aaye, toh iska matlab hai ki cookies purani ho gayi hain. Browser se nayi cookies.txt upload karein.")
