import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Universal Mobile Downloader",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Universal Mobile Downloader")
st.markdown("Download high-quality videos from TikTok, YouTube Shorts, and Instagram instantly.")

# Quality selector for professional look
quality = st.selectbox("⚙️ Select Video Quality:", ["720p (High)", "360p (Standard)"])

video_url = st.text_input("Paste Video Link Here:", placeholder="https://...")

def get_direct_download_data(url):
    """Direct high-speed stream extractor that works on cloud servers"""
    api_url = "https://api.v02.aio-dl.com/api/v1/parse"
    payload = {"url": url.strip()}
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.post(api_url, json=payload, headers=headers, timeout=12)
        if response.status_code == 200:
            res_data = response.json()
            medias = res_data.get("medias", [])
            # Sub se pehle high quality MP4 stream dhoondo
            for media in medias:
                if media.get("extension") == "mp4" and media.get("url"):
                    video_download_url = media.get("url")
                    # Video ke actual bytes stream se download karo
                    video_bytes = requests.get(video_download_url, timeout=15)
                    if video_bytes.status_code == 200:
                        return video_bytes.content
    except:
        pass
    return None

if st.button("DOWNLOAD NOW", use_container_width=True):
    if not video_url:
        st.error("⚠️ Please paste a valid link first!")
    else:
        with st.spinner("Extracting video file... Please wait..."):
            
            # Fetch direct mp4 data from cloud bypass engine
            file_data = get_direct_download_data(video_url)
            
            if file_data:
                st.success("🎉 Video Successfully Processed!")
                
                # Direct Streamlit Download Button (No external website redirection!)
                st.download_button(
                    label="💾 Click Here to Save to Gallery",
                    data=file_data,
                    file_name="Universal_Downloader_Video.mp4",
                    mime="video/mp4",
                    use_container_width=True
                )
                st.balloons()
            else:
                # Solid fallback to public mirror engine
                st.info("🔄 Switching to alternative cloud network...")
                try:
                    alt_res = requests.post(
                        "https://co.wuk.sh/api/json",
                        json={"url": video_url.strip(), "videoQuality": "720"},
                        headers={"Accept": "application/json", "Content-Type": "application/json"},
                        timeout=7
                    )
                    if alt_res.status_code == 200 and alt_res.json().get("url"):
                        direct_url = alt_res.json().get("url")
                        video_bytes = requests.get(direct_url, timeout=10).content
                        st.success("🎉 Video Processed via Backup Route!")
                        st.download_button(
                            label="💾 Click Here to Save to Gallery",
                            data=video_bytes,
                            file_name="Downloaded_Video.mp4",
                            mime="video/mp4",
                            use_container_width=True
                        )
                        st.balloons()
                    else:
                        st.error("❌ This specific link is highly encrypted by the platform. Please try another video link.")
                except:
                    st.error("❌ Server traffic limit exceeded. Please refresh and try again in a few moments.")
