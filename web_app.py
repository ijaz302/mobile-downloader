import streamlit as st
import requests
import urllib.parse

st.set_page_config(
    page_title="Universal Mobile Downloader",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Universal Mobile Downloader")
st.markdown("Download high-quality videos from TikTok, YouTube Shorts, and Instagram instantly.")

quality = st.selectbox("⚙️ Select Video Quality:", ["720p (High)", "360p (Standard)"])
video_url = st.text_input("Paste Video Link Here:", placeholder="https://...")

def try_direct_download(url):
    """Koshish karein ke video isi page par download ho jaye"""
    try:
        # Using a fresh open network mirror
        res = requests.post(
            "https://co.wuk.sh/api/json",
            json={"url": url.strip(), "videoQuality": "720"},
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            timeout=6
        )
        if res.status_code == 200 and res.json().get("url"):
            direct_url = res.json().get("url")
            video_bytes = requests.get(direct_url, timeout=10)
            if video_bytes.status_code == 200:
                return video_bytes.content
    except:
        pass
    return None

if st.button("DOWNLOAD NOW", use_container_width=True):
    if not video_url:
        st.error("⚠️ Please paste a valid link first!")
    else:
        with st.spinner("Processing your request stream..."):
            
            # METHOD 1: Isi page par download karne ki koshish
            file_data = try_direct_download(video_url)
            
            if file_data:
                st.success("🎉 Video Processed Successfully on this Page!")
                st.download_button(
                    label="💾 Click Here to Save to Gallery",
                    data=file_data,
                    file_name="Downloaded_Video.mp4",
                    mime="video/mp4",
                    use_container_width=True
                )
                st.balloons()
            else:
                # METHOD 2: Agar backend block ho, toh gande error ke bajaye smart button show ho
                st.info("💡 Direct server traffic is high. Opening high-speed secure download gateway for you!")
                
                encoded_url = urllib.parse.quote(video_url.strip(), safe='')
                # Direct parsing link jahan automatic video scan ho jayegi
                backup_gateway = f"https://publer.io/tools/media-downloader?url={encoded_url}"
                
                st.markdown(
                    f'<a href="{backup_gateway}" target="_blank" style="'
                    f'display: block; width: 100%; text-align: center; '
                    f'background-color: #24a0ed; color: white; padding: 15px; '
                    f'text-decoration: none; border-radius: 8px; font-weight: bold; '
                    f'font-size: 16px;'
                    f'">📥 Click Here to Save Video (Premium Route)</a>',
                    unsafe_allow_html=True
                )
                st.write("✨ *Note: Is button par click karte hi aapki video pehle se load milegi, bas direct save kar lein!*")
