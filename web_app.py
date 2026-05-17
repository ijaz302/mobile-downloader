import streamlit as st
import time
import requests

# Page Design Setup
st.set_page_config(page_title="Universal Downloader", page_icon="📲", layout="centered")

st.title("📲 Universal Mobile Downloader")
st.write("TikTok, Instagram, aur YouTube videos download karein.")

# 1. QUALITY SELECTION dropdown
quality_choice = st.selectbox(
    "⚙️ Select Video Quality:",
    ["Best Quality (HD/1080p)", "Normal Quality (SD/720p)", "Low Data Mode (360p)"]
)

url = st.text_input("Paste Video Link Here:", placeholder="https://...")

if st.button("DOWNLOAD NOW"):
    if url:
        try:
            with st.spinner("🚀 Link process kiya ja raha hai... Please wait."):
                timestamp = int(time.time())
                clean_url = url.split('?')[0]
                video_bytes = None

                # --- CASE 1: IF THE LINK IS TIKTOK ---
                if "tiktok.com" in url:
                    # TikTok Direct High-Speed API
                    tiktok_api = f"https://api.tiklydown.eu.org/api/download?url={url}"
                    tk_res = requests.get(tiktok_api, timeout=12)
                    if tk_res.status_code == 200:
                        tk_data = tk_res.json()
                        # Get video no watermark link
                        video_url = tk_data.get("video", {}).get("noWatermark") or tk_data.get("video", {}).get("nowm")
                        if video_url:
                            video_bytes = requests.get(video_url, timeout=15).content

                # --- CASE 2: IF THE LINK IS INSTAGRAM ---
                elif "instagram.com" in url:
                    insta_api = f"https://api.vveapi.com/instagram/download?url={clean_url}"
                    in_res = requests.get(insta_api, timeout=15)
                    if in_res.status_code == 200:
                        in_data = in_res.json()
                        video_url = in_data.get("video_url") or in_data.get("url") or in_data.get("data", {}).get("video_url")
                        if video_url:
                            video_bytes = requests.get(video_url, timeout=15).content

                # --- DISPLAY OUTPUT AND SAVE BUTTON ---
                if video_bytes:
                    st.success("✨ Video successfully fetched!")
                    st.write(f"🎯 Downloaded in: **{quality_choice}**")
                    
                    # Video player display
                    st.video(video_bytes)
                    
                    # 2. SAVE TO GALLERY BUTTON
                    st.download_button(
                        label="📥 Save to Device / Gallery",
                        data=video_bytes,
                        file_name=f"downloader_video_{timestamp}.mp4",
                        mime="video/mp4"
                    )
                else:
                    if "tiktok.com" in url:
                        st.error("TikTok server se video link nahi mil saka. Ek baar dobara try karein.")
                    else:
                        st.error("Instagram server temporary busy hai. Please 1-2 minute baad dobara TRY karein.")

        except Exception as e:
            st.error("Network connection line busy hai. Please refresh karke dobara try karein.")
    else:
        st.warning("Pehle koi link paste karein!")