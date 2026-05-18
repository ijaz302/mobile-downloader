import streamlit as st
import requests

st.set_page_config(
    page_title="Universal Mobile Downloader",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Universal Mobile Downloader")
st.markdown("Download high-quality videos from TikTok and YouTube instantly.")

st.info("💡 Copy your video link, paste it below, and get a direct download link instantly!")

video_url = st.text_input("Paste Video Link Here:", placeholder="https://...")

if st.button("DOWNLOAD NOW", use_container_width=True):
    if not video_url:
        st.error("⚠️ Please paste a valid link first!")
    else:
        with st.spinner("Processing video via premium bypass server... Please wait..."):
            try:
                # Clean URL (extra parameters hatane ke liye)
                clean_url = video_url.split("?")[0].strip()
                
                # Using a very stable public Cobalt API instance
                cobalt_api_url = "https://api.cobalt.tools/"
                
                payload = {
                    "url": clean_url,
                    "videoQuality": "720", # 720p is highly compatible and fast
                    "isNoTTWatermark": True
                }
                
                headers = {
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                }
                
                response = requests.post(cobalt_api_url, json=payload, headers=headers, timeout=15)
                
                if response.status_code == 200:
                    data = response.json()
                    status = data.get("status")
                    
                    if status in ["redirect", "stream"]:
                        download_link = data.get("url")
                        
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
                    elif status == "error":
                        st.error(f"❌ Server Error: {data.get('text', 'Could not process video.')}")
                    else:
                        st.error("⚠️ Unexpected response. Please try a different link.")
                else:
                    st.error(f"🔒 Platform Security Block (Status {response.status_code}). Please try a YouTube or TikTok link.")
                    
            except Exception as e:
                st.error(f"⚠️ An unexpected error occurred: {str(e)}")
