import streamlit as st
import requests
import re

st.set_page_config(
    page_title="Universal Mobile Downloader",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Universal Mobile Downloader")
st.markdown("Download high-quality videos from TikTok and YouTube instantly.")

video_url = st.text_input("Paste Video Link Here:", placeholder="https://...")

def extract_video_id(url):
    """YouTube URL se Video ID nikalne ka tareeqa"""
    match = re.search(r'(?:v=|\/shorts\/|\/embed\/|\/v\/|youtu\.be\/|\/v=|^)([^#\&\?^\/]+)', url)
    return match.group(1) if match else None

# 1️⃣ METHOD A: Cobalt API Instance 1
def try_cobalt_primary(url):
    try:
        response = requests.post(
            "https://api.cobalt.tools/",
            json={"url": url, "videoQuality": "720", "isNoTTWatermark": True},
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            timeout=8
        )
        if response.status_code == 200 and response.json().get("status") in ["redirect", "stream"]:
            return response.json().get("url")
    except:
        pass
    return None

# 2️⃣ METHOD B: Cobalt API Alternative Instance 2
def try_cobalt_secondary(url):
    try:
        response = requests.post(
            "https://co.wuk.sh/api/json",
            json={"url": url, "videoQuality": "720"},
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            timeout=8
        )
        if response.status_code == 200 and response.json().get("url"):
            return response.json().get("url")
    except:
        pass
    return None

# 3️⃣ METHOD C: Invidious API Server (Sirf YouTube ke liye specialized)
def try_invidious(url):
    video_id = extract_video_id(url)
    if not video_id:
        return None
    # 3 mukhtalif public invidious servers check karega auto-rotation mein
    servers = ["https://invidious.nerdvpn.de", "https://yewtu.be", "https://iv.melmac.space"]
    for server in servers:
        try:
            res = requests.get(f"{server}/api/v1/videos/{video_id}", timeout=5)
            if res.status_code == 200:
                streams = res.json().get("formatStreams", [])
                if streams:
                    return streams[0].get("url")
        except:
            continue
    return None

if st.button("DOWNLOAD NOW", use_container_width=True):
    if not video_url:
        st.error("⚠️ Please paste a valid link first!")
    else:
        with st.spinner("Connecting to secure high-speed download servers..."):
            download_link = None
            
            # Sub se pehle Primary Server check karo
            download_link = try_cobalt_primary(video_url)
            
            # Agar primary fail ho, toh Secondary Server check karo
            if not download_link:
                download_link = try_cobalt_secondary(video_url)
                
            # Agar dono fail hon aur link YouTube ka ho, toh Invidious direct stream uthao
            if not download_link and ("youtube" in video_url or "youtu.be" in video_url):
                download_link = try_invidious(video_url)

            # Final Result Display
            if download_link:
                st.success("🎉 Video Successfully Processed!")
                st.markdown(
                    f'<a href="{download_link}" target="_blank" style="'
                    f'display: block; width: 100%; text-align: center; '
                    f'background-color: #24a0ed; color: white; padding: 12px; '
                    f'text-decoration: none; border-radius: 5px; font-weight: bold;'
                    f'">📥 Click Here to Save Video</a>',
                    unsafe_allow_code=True
                )
                st.balloons()
            else:
                st.error("❌ Servers are busy right now due to high traffic. Please refresh or try another link in a few moments.")
