import streamlit as st
import yt_dlp
import os
import subprocess
import sys

# yt-dlp ko latest features ke sath active rakhne ke liye
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"])
except Exception as e:
    pass

st.set_page_config(
    page_title="Universal Mobile Downloader",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Universal Mobile Downloader")
st.markdown("Download high-quality videos from TikTok, Instagram, and YouTube instantly.")

quality = st.selectbox(
    "⚙️ Select Video Quality:",
    ["Best Quality (HD/1080p)", "Standard Quality (SD/480p)"]
)

video_url = st.text_input("Paste Video Link Here:", placeholder="https://...")

if st.button("DOWNLOAD NOW", use_container_width=True):
    if not video_url:
        st.error("⚠️ Please paste a valid link first!")
    else:
        with st.spinner("Processing video... Please wait..."):
            try:
                if "Best" in quality:
                    format_option = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
                else:
                    format_option = 'worst[ext=mp4]/worst'
                
                output_template = 'downloaded_video.mp4'
                
                ydl_opts = {
                    'format': format_option,
                    'quiet': True,
                    'no_warnings': True,
                    'outtmpl': output_template,
                    'merge_output_format': 'mp4',
                    # Agar aap cookies text file banati hain toh yeh khud hi utha lega
                    'cookiefile': 'cookies.txt' if os.path.exists('cookies.txt') else None,
                    'extractor_args': {
                        'youtube': {
                            'player_client': ['android', 'web'],
                            'skip': ['dash', 'hls']
                        },
                        'tiktok': {'web_page': True},
                        'instagram': {'check_connection': True}
                    },
                    'http_headers': {
                        # Instagram mobile requests ko zyada bypass karta hai
                        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Connection': 'keep-alive',
                    }
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(video_url, download=True)
                    filename = output_template if os.path.exists(output_template) else ydl.prepare_filename(info_dict)
                    video_title = info_dict.get('title', 'Downloaded Video')

                if os.path.exists(filename):
                    with open(filename, "rb") as file:
                        video_bytes = file.read()
                    
                    st.success(f"🎉 Video Successfully Fetched: **{video_title}**")
                    
                    st.download_button(
                        label="💾 Click Here to Save to Your Device",
                        data=video_bytes,
                        file_name="Universal_Downloader_Video.mp4",
                        mime="video/mp4",
                        use_container_width=True
                    )
                    
                    os.remove(filename)
                else:
                    st.error("❌ File processing error. Please try again.")

            except yt_dlp.utils.DownloadError as e:
                st.error(f"🔒 Security Block: {str(e)}")
            except Exception as e:
                st.error(f"⚠️ An unexpected error occurred: {str(e)}")
