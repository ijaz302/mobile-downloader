import streamlit as st
import yt_dlp

st.set_page_config(page_title="TikTok Downloader")
st.title("TikTok Video Downloader")

url = st.text_input("Enter TikTok URL here")

if url:
    if st.button("Download"):
        try:
            st.write("Processing... please wait.")
            # TikTok ke liye koi cookies ki zaroorat nahi
            ydl_opts = {
                'format': 'best',
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
            
            with open(filename, "rb") as file:
                st.download_button(
                    label="Download Video",
                    data=file,
                    file_name=filename,
                    mime="video/mp4"
                )
            st.success("Download ready!")
                
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Tip: Sirf TikTok ka link daalein.")
