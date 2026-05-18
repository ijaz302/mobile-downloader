import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="Universal Mobile Downloader",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Universal Mobile Downloader")
st.markdown("Download high-quality videos from TikTok and YouTube instantly.")

st.warning("⚡ Premium High-Speed Downloading Gateway Active!")

video_url = st.text_input("Paste Video Link Here:", placeholder="https://...")

if st.button("DOWNLOAD NOW", use_container_width=True):
    if not video_url:
        st.error("⚠️ Please paste a valid link first!")
    else:
        with st.spinner("Generating your secure download stream..."):
            # URL ko safe format mein convert karne ke liye
            encoded_url = urllib.parse.quote(video_url.strip(), safe='')
            
            # Direct link generate karna
            bypass_download_url = f"https://cobalt.tools/?url={encoded_url}"
            
            st.success("🎉 Download Link Successfully Generated!")
            
            # FIXED LINE: Changed unsafe_allow_code to unsafe_allow_html
            st.markdown(
                f'<a href="{bypass_download_url}" target="_blank" style="'
                f'display: block; width: 100%; text-align: center; '
                f'background-color: #24a0ed; color: white; padding: 15px; '
                f'text-decoration: none; border-radius: 8px; font-weight: bold; '
                f'font-size: 16px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);'
                f'">📥 Click Here to Download & Save Video</a>',
                unsafe_allow_html=True
            )
            
            st.info("💡 Note: Upar wale button par click karte hi aapki video direct fetch ho jayegi, bas wahan download arrow par click kar lein!")
            st.balloons()
