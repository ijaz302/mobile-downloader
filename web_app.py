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
                # Using open-source robust Cobalt API instances
                cobalt_api_url = "https://api.cobalt.tools/"
                
                payload = {
                    "url": video_url,
                    "videoQuality": "1080", # Best quality format
                    "audioFormat": "mp3",
                    "isAudioOnly": False,
                    "isNoTTWatermark": True # TikTok without watermark
                }
                
                headers = {
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                }
                
                response = requests.post(cobalt_api_url, json=payload, headers=headers, timeout=15)
                
                if response.status_code == 200:
                    data = response.json()
                    status = data.get("status")
                    
                    if status == "redirect" or status == "stream":
                        download_link = data.get("url")
                        
                        st.success("🎉 Video Successfully Processed!")
                        # Creating a clear beautiful download button link
                        st.markdown(
                            f'<a href="{download_link}" target="_blank" style="'
                            f'display: block; width: 100%; text-align: center; '
                            f'background-color: #24a0ed; color: white; padding: 10px; '
                            f'text-decoration: none; border-radius: 5px; font-weight: bold;'
                            f'">📥 Click Here to Save Video to Your Device</a>',
                            unsafe_allow_code=True
                        )
                        st.balloons()
                    elif status == "error":
                        st.error(f"❌ Server Error: {data.get('text', 'Could not process video.')}")
                    else:
                        st.error("⚠️ Unexpected response from download server. Please try again.")
                else:
                    st.error(f"🔒 Security Block: Cloud server rejected request (Status Code: {response.status_code})")
                    
            except requests.exceptions.Timeout:
                st.error("⏱️ Connection timeout! The video platform took too long to respond. Please try again.")
            except Exception as e:
                st.error(f"⚠️ An unexpected error occurred: {str(e)}")
