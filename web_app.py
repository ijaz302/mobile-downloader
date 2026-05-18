import streamlit as st
import requests

st.set_page_config(
    page_title="Universal Mobile Downloader",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Universal Mobile Downloader")
st.markdown("Download high-quality videos from TikTok and YouTube instantly.")

video_url = st.text_input("Paste Video Link Here:", placeholder="https://...")

def download_via_aio(url):
    """Stable All-In-One Downloader API Engine"""
    try:
        # Public legal high-speed video processing gateway
        api_url = "https://api.v02.aio-dl.com/api/v1/parse"
        payload = {"url": url}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36"
        }
        
        response = requests.post(api_url, json=payload, headers=headers, timeout=12)
        if response.status_code == 200:
            data = response.json()
            # Streams list mein se check karna
            medias = data.get("medias", [])
            for media in medias:
                if media.get("extension") == "mp4" or media.get("type") == "video":
                    return media.get("url")
    except:
        pass
    return None

if st.button("DOWNLOAD NOW", use_container_width=True):
    if not video_url:
        st.error("⚠️ Please paste a valid link first!")
    else:
        with st.spinner("Processing video through secure stream servers..."):
            
            # Fetch direct link from stable network
            download_link = download_via_aio(video_url)
            
            # Final Check
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
                st.error("❌ Link could not be fetched due to server traffic. Please try after 1 minute or try a different link.")
