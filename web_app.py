import streamlit as st
import os
import time
import requests

# Page Settings (Khoobsurat interface ke liye)
st.set_page_config(page_title="Universal Downloader", page_icon="📲", layout="centered")

st.title("📲 Universal Mobile Downloader")
st.write("TikTok, Instagram, aur YouTube videos download karein.")

# 1. QUALITY SELECTION OPTION (Aapki pasand ki quality)
quality_choice = st.selectbox(
    "⚙️ Select Video Quality:",
    ["Best Quality (HD/1080p)", "Normal Quality (SD/720p)", "Low Data Mode (360p)"]
)

# Input Box
url = st.text_input("Paste Video Link Here:", placeholder="https://www.instagram.com/... ")

if st.button("DOWNLOAD NOW"):
    if url:
        try:
            with st.spinner("Processing... Server security ko bypass kiya ja raha hai."):
                timestamp = int(time.time())
                clean_url = url.split('?')[0]
                video_url = None

                # --- SERVER 1: Direct Fetch Engine ---
                try:
                    api_1 = f"https://api.vvesc.com/instagram?url={clean_url}"
                    res_1 = requests.get(api_1, timeout=7).json()
                    if res_1.get('url'):
                        video_url = res_1.get('url')
                except:
                    pass

                # --- SERVER 2: Backup Premium Line ---
                if not video_url:
                    try:
                        api_2 = f"https://api.bhadooo.com/instagram/v1/downloader?url={clean_url}"
                        res_2 = requests.get(api_2, timeout=7).json()
                        video_url = res_2.get("data", [{}])[0].get("url") or res_2.get("url")
                    except:
                        pass

                # --- OUTPUT SECTION ---
                if video_url:
                    # Video data download ho raha hai
                    video_bytes = requests.get(video_url, timeout=12).content
                    
                    st.success("✨ Video successfully fetched!")
                    st.write(f"🎯 Selected Mode: **{quality_choice}**")
                    
                    # Video Player Display
                    st.video(video_bytes)
                    
                    # 2. DOWNLOAD BUTTON (Direct Gallery mein save karne ke liye)
                    st.download_button(
                        label="📥 Save to Device / Gallery",
                        data=video_bytes,
                        file_name=f"download_{timestamp}.mp4",
                        mime="video/mp4"
                    )
                else:
                    st.error("Instagram ka free server is waqt busy hai. Please 1-2 minute baad dobara TRY karein ya koi doosra link check karein.")

        except Exception as e:
            st.error("Connection temporary lost! Please page ko refresh (reload) karke dobara check karein.")
    else:
        st.warning("Pehle koi link paste karein!")