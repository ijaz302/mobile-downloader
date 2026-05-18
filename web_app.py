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

def download_via_premium_gateway(url):
    """SaveFrom API gateway jo kabhi block nahi hota"""
    try:
        api_url = "https://worker.sf-api.com/savefrom.php"
        payload = {"url": url}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Origin": "https://en.savefrom.net",
            "Referer": "https://en.savefrom.net/"
        }
        response = requests.post(api_url, data=payload, headers=headers, timeout=12)
        if response.status_code == 200:
            # Response mein se video link extract karna
            text = response.text
            links = re.findall(r'url["\']\s*:\s*["\'](http[^"\']+)["\']', text)
            if links:
                return links[0]
    except:
        pass
    return None

if st.button("DOWNLOAD NOW", use_container_width=True):
    if not video_url:
        st.error("⚠️ Please paste a valid link first!")
    else:
        with st.spinner("Bypassing platform security... Fetching your video..."):
            # Try Premium Gateway first
            download_link = download_via_premium_gateway(video_url)
            
            # Backup: Simple alternative scrap if premium lags
            if not download_link:
                try:
                    res = requests.post("https://api.cobalt.tools/", json={"url": video_url, "videoQuality": "720"}, timeout=5)
                    if res.status_code == 200 and res.json().get("status") in ["redirect", "stream"]:
                        download_link = res.json().get("url")
                except:
                    pass

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
                st.error("❌ Link is protected or temporary unavailable. Please check the link or try another one.")
