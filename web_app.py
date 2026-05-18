import streamlit as st
import requests
import os

st.set_page_config(
    page_title="Universal Mobile Downloader",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Universal Mobile Downloader")
st.markdown("Download high-quality videos from TikTok, YouTube, and Instagram instantly.")

# 1️⃣ Quality Selection Button Wapas Aa Gaya
quality = st.selectbox(
    "⚙️ Select Video Quality:",
    ["1080p (Best Quality)", "720p (High Quality)", "480p (Standard Quality)", "360p (Low Quality)"]
)

video_url = st.text_input("Paste Video Link Here:", placeholder="https://...")

def fetch_video_bytes(url, q_val):
    """Direct backend se video fetch karne ka tareeqa"""
    # Map selection to cobalt quality strings
    q_map = {
        "1080p (Best Quality)": "1080",
        "720p (High Quality)": "720",
        "480p (Standard Quality)": "480",
        "360p (Low Quality)": "360"
    }
    api_quality = q_map.get(q_val, "720")
    
    # Alag alag working mirrors takay block na ho
    endpoints = ["https://api.cobalt.tools/", "https://co.wuk.sh/api/json"]
    
    for api_url in endpoints:
        try:
            payload = {
                "url": url.strip(),
                "videoQuality": api_quality,
                "isNoTTWatermark": True
            }
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
            response = requests.post(api_url, json=payload, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                video_stream_url = data.get("url")
                
                if video_stream_url:
                    # Direct file data download karna stream se
                    video_res = requests.get(video_stream_url, timeout=15)
                    if video_res.status_code == 200:
                        return video_res.content
        except:
            continue
    return None

if st.button("DOWNLOAD NOW", use_container_width=True):
    if not video_url:
        st.error("⚠️ Please paste a valid link first!")
    else:
        with st.spinner("Processing video data... Please wait..."):
            
            video_bytes = fetch_video_bytes(video_url, quality)
            
            if video_bytes:
                st.success("🎉 Video Successfully Processed!")
                
                # 2️⃣ Direct Save to Device/Gallery Button Wapas Aa Gaya
                st.download_button(
                    label="💾 Click Here to Save Video to Gallery",
                    data=video_bytes,
                    file_name="Universal_Downloader_Video.mp4",
                    mime="video/mp4",
                    use_container_width=True
                )
                st.balloons()
            else:
                st.error("❌ High traffic block on cloud servers. Please try again after a brief moment or try a different link.")
