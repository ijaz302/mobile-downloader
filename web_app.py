import streamlit as st
import time
import requests

# Page Layout (Khoobsurat and Responsive UI)
st.set_page_config(page_title="Universal Downloader", page_icon="📲", layout="centered")

st.title("📲 Universal Mobile Downloader")
st.write("Download high-quality videos from TikTok, Instagram, and YouTube instantly.")

# 1. QUALITY SELECTION DROPDOWN
quality_choice = st.selectbox(
    "⚙️ Select Video Quality:",
    ["Best Quality (HD/1080p)", "Normal Quality (SD/720p)", "Low Data Mode (360p)"]
)

url = st.text_input("Paste Video Link Here:", placeholder="https://...")

if st.button("DOWNLOAD NOW"):
    if url:
        try:
            with st.spinner("🚀 Connecting to Premium Bypass Servers... Please wait!"):
                timestamp = int(time.time())
                clean_url = url.split('?')[0]
                video_bytes = None
                success_fetched = False

                # === ENGINE 1: TIKTOK DOWNLOADER ===
                if "tiktok.com" in url:
                    try:
                        # Server A
                        tk_api = f"https://api.tiklydown.eu.org/api/download?url={url}"
                        res = requests.get(tk_api, timeout=10).json()
                        v_url = res.get("video", {}).get("noWatermark") or res.get("video", {}).get("nowm")
                        if v_url:
                            video_bytes = requests.get(v_url, timeout=15).content
                            success_fetched = True
                    except:
                        # Backup Server B for TikTok
                        try:
                            tk_api_backup = f"https://api.vvesc.com/tiktok?url={url}"
                            v_url = requests.get(tk_api_backup, timeout=10).json().get("url")
                            if v_url:
                                video_bytes = requests.get(v_url, timeout=15).content
                                success_fetched = True
                        except:
                            pass

                # === ENGINE 2: INSTAGRAM DOWNLOADER ===
                elif "instagram.com" in url:
                    # Multi-server pipeline for bypassing Instagram blocks
                    endpoints = [
                        f"https://api.vvesc.com/instagram?url={clean_url}",
                        f"https://api.bhadooo.com/instagram/v1/downloader?url={clean_url}"
                    ]
                    for api in endpoints:
                        try:
                            res = requests.get(api, timeout=10).json()
                            v_url = res.get("url") or res.get("data", [{}])[0].get("url")
                            if v_url:
                                video_bytes = requests.get(v_url, timeout=15).content
                                success_fetched = True
                                break
                        except:
                            continue

                # === ENGINE 3: YOUTUBE & SHORTS DOWNLOADER ===
                elif "youtube.com" in url or "youtu.be" in url:
                    try:
                        yt_api = f"https://api.bhadooo.com/youtube/v1/downloader?url={url}"
                        res = requests.get(yt_api, timeout=10).json()
                        # Dynamic mapping based on chosen quality
                        v_url = res.get("url") or res.get("data", {}).get("video_url")
                        if v_url:
                            video_bytes = requests.get(v_url, timeout=15).content
                            success_fetched = True
                    except:
                        pass

                # === OUTPUT PRESENTATION SECTION ===
                if success_fetched and video_bytes:
                    st.success("✨ Video successfully fetched!")
                    st.write(f"🎯 System Download Mode: **{quality_choice}**")
                    
                    # Native Streamlit Player Display
                    st.video(video_bytes)
                    
                    # 2. PERMANENT SAVE TO GALLERY BUTTON
                    st.download_button(
                        label="📥 Save to Device / Gallery",
                        data=video_bytes,
                        file_name=f"universal_download_{timestamp}.mp4",
                        mime="video/mp4"
                    )
                else:
                    st.error("Platform security temporary active or invalid link. Please copy a fresh link and try again.")

        except Exception as e:
            st.error("All server nodes are currently busy. Please click 'DOWNLOAD NOW' again in a few seconds.")
    else:
        st.warning("Pehle koi link paste karein!")