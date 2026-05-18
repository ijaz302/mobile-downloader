import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="Universal Mobile Downloader",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Universal Mobile Downloader")
st.markdown("Download high-quality videos from TikTok, YouTube, and Instagram instantly.")

st.warning("⚡ Premium High-Speed Downloading Gateway Active!")

video_url = st.text_input("Paste Video Link Here:", placeholder="https://...")

if st.button("DOWNLOAD NOW", use_container_width=True):
    if not video_url:
        st.error("⚠️ Please paste a valid link first!")
    else:
        with st.spinner("Bypassing firewalls... Generating high-speed download button..."):
            
            clean_url = video_url.strip()
            
            # SaveFrom Net ka official bypass url generator
            # Yeh hamesha chalta hai aur isme quality aur gallery save option khud hi aa jata hai
            bypass_download_url = f"https://en.savefrom.net/1-youtube-video-downloader-360v/?url={urllib.parse.quote(clean_url)}"
            
            st.success("🎉 Download Link Successfully Generated!")
            
            # Beautiful Blue Download Button
            st.markdown(
                f'<a href="{bypass_download_url}" target="_blank" style="'
                f'display: block; width: 100%; text-align: center; '
                f'background-color: #24a0ed; color: white; padding: 15px; '
                f'text-decoration: none; border-radius: 8px; font-weight: bold; '
                f'font-size: 16px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);'
                f'">📥 Click Here to Download & Save Video</a>',
                unsafe_allow_html=True
            )
            
            st.info("💡 Note: Button par click karte hi SaveFrom ka premium gateway khulega jahan aapko 1080p/720p quality select karne aur direct Gallery mein Save karne ka option mil jayegi!")
            st.balloons()
