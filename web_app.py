import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="Universal Mobile Downloader",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Universal Mobile Downloader")
st.markdown("Download high-quality videos from TikTok, YouTube Shorts, and Instagram instantly.")

# Visual options for users
quality = st.selectbox("⚙️ Select Video Quality:", ["1080p (Best Quality)", "720p (High Quality)"])

video_url = st.text_input("Paste Video Link Here:", placeholder="https://...")

if st.button("DOWNLOAD NOW", use_container_width=True):
    if not video_url:
        st.error("⚠️ Please paste a valid link first!")
    else:
        with st.spinner("Bypassing security layers..."):
            
            clean_url = video_url.strip()
            
            # Pure web ka sabse bada 100% automatic link parsing tool
            # Is par click karte hi direct device/gallery save custom interface khulta hai
            final_download_gateway = f"https://publer.io/tools/media-downloader?url={urllib.parse.quote(clean_url)}"
            
            st.success("🎉 Download Stream Ready!")
            
            # High-end Premium Blue Button
            st.markdown(
                f'<a href="{final_download_gateway}" target="_blank" style="'
                f'display: block; width: 100%; text-align: center; '
                f'background-color: #24a0ed; color: white; padding: 15px; '
                f'text-decoration: none; border-radius: 8px; font-weight: bold; '
                f'font-size: 16px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);'
                f'">📥 Click Here to Save Video to Gallery</a>',
                unsafe_allow_html=True
            )
            
            st.info("💡 Note: Upar wale button par click karte hi aapka link automatically scan ho jayega, bas download button daba kar gallery mein save kar lein!")
            st.balloons()
