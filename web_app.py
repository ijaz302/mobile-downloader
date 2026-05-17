import streamlit as st
import yt_dlp
import os
import time
import requests

st.set_page_config(page_title="Universal Downloader", page_icon="📲", layout="centered")

st.title("📲 Universal Mobile Downloader")
st.write("TikTok, Instagram, aur YouTube videos download karein.")

url = st.text_input("Paste Video Link Here:", placeholder="https://...")

if st.button("DOWNLOAD NOW"):
    if url:
        try:
            with st.spinner("Processing... High-Quality video fetch ki ja rahi hai."):
                timestamp = int(time.time())
                unique_filename = f"video_{timestamp}.mp4"
                video_data = None

                # Special Bypass for Instagram Links
                if "instagram.com" in url:
                    # Backup Method 1: Rapid API-free Endpoint
                    try:
                        api_url = f"https://api.vvesc.com/instagram?url={url}"
                        res = requests.get(api_url, timeout=8)
                        if res.status_code == 200 and res.json().get('url'):
                            video_data = requests.get(res.json().get('url'), timeout=10).content
                    except:
                        pass

                # If Instagram special bypass didn't run, use the general high-quality downloader
                if video_data is None:
                    ydl_opts = {
                        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                        'outtmpl': unique_filename,
                        'quiet': True,
                        'no_warnings': True,
                        'geo_bypass': True,
                        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                    }

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])

                    if os.path.exists(unique_filename):
                        with open(unique_filename, "rb") as f:
                            video_data = f.read()
                        os.remove(unique_filename)

                # --- Displaying Output, Quality Info, and Save Button ---
                if video_data:
                    st.success("✨ Video successfully fetched in best available quality!")
                    
                    # 1. Quality Display Info
                    st.info("⚙️ Quality: **Auto-Selected Best (HD/MP4)**")
                    
                    # 2. Player Display
                    st.video(video_data)
                    
                    # 3. Save to Gallery Button
                    st.download_button(
                        label="📥 Save to Device / Gallery",
                        data=video_data,
                        file_name=f"download_{timestamp}.mp4",
                        mime="video/mp4"
                    )
                else:
                    st.error("Video fetch nahi ho saki. Yeh link temporary restricted hai, please thodi dair baad koi doosra link check karein.")

        except Exception as e:
            st.error(f"Server is busy! Please try a different video link or refresh the page.")
    else:
        st.warning("Pehle koi link paste karein!")
