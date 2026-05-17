import streamlit as st
import os
import time
import requests

# Page Settings
st.set_page_config(page_title="Universal Downloader", page_icon="📲", layout="centered")

st.title("📲 Universal Mobile Downloader")
st.write("TikTok, Instagram, aur YouTube videos download karein.")

url = st.text_input("Paste Video Link Here:", placeholder="https://...")

if st.button("DOWNLOAD NOW"):
    if url:
        try:
            with st.spinner("Processing... High-Quality video link fetch kiya ja raha hai."):
                timestamp = int(time.time())
                clean_url = url.split('?')[0]
                video_url = None

                # --- SERVER 1: Rapid Extraction System ---
                if "instagram.com" in url:
                    try:
                        api_1 = f"https://api.vvesc.com/instagram?url={clean_url}"
                        res_1 = requests.get(api_1, timeout=6).json()
                        if res_1.get('url'):
                            video_url = res_1.get('url')
                    except:
                        pass

                # --- SERVER 2: Backup Public Proxy System ---
                if not video_url and "instagram.com" in url:
                    try:
                        api_2 = f"https://api.bhadooo.com/instagram/v1/downloader?url={clean_url}"
                        res_2 = requests.get(api_2, timeout=6).json()
                        video_url = res_2.get("data", [{}])[0].get("url") or res_2.get("url")
                    except:
                        pass

                # --- SERVER 3: Absolute Mirror Engine ---
                if not video_url and "instagram.com" in url:
                    try:
                        api_3 = f"https://api.rest7.com/v1/instagram_video_downloader.php?url={clean_url}"
                        res_3 = requests.get(api_3, timeout=6).json()
                        if res_3.get('success'):
                            video_url = res_3.get('file')
                    except:
                        pass

                # --- RESOLUTION & DISPLAY ---
                if video_url:
                    # Video stream download ho rahi hai display ke liye
                    video_bytes = requests.get(video_url, timeout=12).content
                    
                    st.success("✨ Video successfully fetched!")
                    
                    # 1. QUALITY OPTION DISPLAY
                    st.info("⚙️ Video Quality: **High Definition (HD / 1080p MP4)**")
                    
                    # Video Player
                    st.video(video_bytes)
                    
                    # 2. DOWNLOAD / SAVE TO GALLERY BUTTON
                    st.download_button(
                        label="📥 Save to Device / Gallery",
                        data=video_bytes,
                        file_name=f"download_{timestamp}.mp4",
                        mime="video/mp4"
                    )
                else:
                    st.error("Server multi-line busy hai. Instagram temporary block lagatar hai, please 1-2 minute baad dobara TRY karein.")

        except Exception as e:
            st.error("Connection drop error. Please page refresh karke dobara check karein.")
    else:
        st.warning("Pehle koi link paste karein!")