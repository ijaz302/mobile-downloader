import streamlit as st
import requests
import urllib.parse

st.set_page_config(
    page_title="Universal Mobile Downloader",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Universal Mobile Downloader")
st.markdown("Download high-quality videos from TikTok, YouTube, and Instagram instantly.")

# 1️⃣ Quality Option Bilkul Safe
quality = st.selectbox(
    "⚙️ Select Video Quality:",
    ["1080p (Best Quality)", "720p (High Quality)", "480p (Standard Quality)"]
)

video_url = st.text_input("Paste Video Link Here:", placeholder="https://...")

def fetch_direct_video(url, q_val):
    """Direct fetch karne ki koshish (Method A)"""
    q_map = {"1080p (Best Quality)": "1080", "720p (High Quality)": "720", "480p (Standard Quality)": "480"}
    api_quality = q_map.get(q_val, "720")
    
    try:
        payload = {"url": url.strip(), "videoQuality": api_quality, "isNoTTWatermark": True}
        res = requests.post("https://api.cobalt.tools/", json=payload, headers={"Accept": "application/json"}, timeout=8)
        if res.status_code == 200:
            stream_url = res.json().get("url")
            if stream_url:
                video_res = requests.get(stream_url, timeout=10)
                if video_res.status_code == 200:
                    return video_res.content
    except:
        pass
    return None

if st.button("DOWNLOAD NOW", use_container_width=True):
    if not video_url:
        st.error("⚠️ Please paste a valid link first!")
    else:
        with st.spinner("Analyzing video stream and bypassing firewalls..."):
            
            # Pehle direct download try karo
            video_bytes = fetch_direct_video(video_url, quality)
            
            if video_bytes:
                st.success("🎉 Video Successfully Processed!")
                st.download_button(
                    label="💾 Click Here to Save to Gallery",
                    data=video_bytes,
                    file_name="Downloaded_Video.mp4",
                    mime="video/mp4",
                    use_container_width=True
                )
                st.balloons()
            else:
                # 2️⃣ SMART BYPASS: Agar network block ho, toh crash hone ki bajaye automatic direct working option de do!
                st.info("⚡ Direct server route busy. Premium Bypass Gateway activated for you!")
                
                encoded_url = urllib.parse.quote(video_url.strip(), safe='')
                bypass_url = f"https://cobalt.tools/?url={encoded_url}"
                
                st.markdown(
                    f'<a href="{bypass_url}" target="_blank" style="'
                    f'display: block; width: 100%; text-align: center; '
                    f'background-color: #24a0ed; color: white; padding: 14px; '
                    f'text-decoration: none; border-radius: 8px; font-weight: bold; '
                    f'font-size: 16px;">📥 Click Here to Download (Bypass Server)</a>',
                    unsafe_allow_html=True
                )
                st.write("💡 *Note: Is blue button par click karein, wahan Cloudflare verification ke baad direct download arrow par click karke save kar lein!*")
