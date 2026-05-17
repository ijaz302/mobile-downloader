import streamlit as st
import yt_dlp
import os

# Page Configuration (Browser tab setting)
st.set_page_config(
    page_title="Universal Mobile Downloader",
    page_icon="📱",
    layout="centered"
)

# App Title & UI
st.title("📱 Universal Mobile Downloader")
st.markdown("Download high-quality videos from TikTok, Instagram, and YouTube instantly.")

# Quality Selection
quality = st.selectbox(
    "⚙️ Select Video Quality:",
    ["Best Quality (HD/1080p)", "Standard Quality (SD/480p)"]
)

# Link Input Box
video_url = st.text_input("Paste Video Link Here:", placeholder="https://...")

# Download Button Clicked
if st.button("DOWNLOAD NOW", use_container_width=True):
    if not video_url:
        st.error("⚠️ Please paste a valid link first!")
    else:
        with st.spinner("Processing video... Please wait..."):
            try:
                # 1. Select format based on user choice
                format_option = 'bestvideo+bestaudio/best' if "Best" in quality else 'worst/worst'
                
                # 2. Advanced yt-dlp Configuration to bypass TikTok/Insta Security
                ydl_opts = {
                    'format': format_option,
                    'quiet': True,
                    'no_warnings': True,
                    'outtmpl': 'downloaded_video.%(ext)s', # Temporary filename
                    # Fake Browser Headers to fool platform security
                    'http_headers': {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Sec-Fetch-Mode': 'navigate',
                        'Connection': 'keep-alive',
                    },
                    # Force web page extraction for TikTok
                    'extractor_args': {
                        'tiktok': {
                            'web_page': True,
                        }
                    }
                }

                # 3. Extract Info and Download Video to Server Memory
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(video_url, download=True)
                    filename = ydl.prepare_filename(info_dict)
                    video_title = info_dict.get('title', 'Downloaded Video')

                # 4. Read the downloaded file into bytes for Streamlit Download Button
                if os.path.exists(filename):
                    with open(filename, "rb") as file:
                        video_bytes = file.read()
                    
                    st.success(f"🎉 Video Successfully Fetched: **{video_title}**")
                    
                    # Actual Download Button for User
                    st.download_button(
                        label="💾 Click Here to Save to Your Device",
                        data=video_bytes,
                        file_name=filename,
                        mime="video/mp4",
                        use_container_width=True
                    )
                    
                    # Delete file from server after loading into memory to save space
                    os.remove(filename)
                else:
                    st.error("❌ File processing error. Please try again.")

            except yt_dlp.utils.DownloadError as e:
                # Catching extraction/security errors specifically
                st.error("🔒 Platform security temporarily active or invalid link. Please copy a fresh link and try again.")
            except Exception as e:
                st.error(f"⚠️ An unexpected error occurred: {str(e)}")