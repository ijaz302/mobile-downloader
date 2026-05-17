import streamlit as st
import time
import requests

# Page Settings
st.set_page_config(page_title="Universal Downloader", page_icon="📲", layout="centered")

st.title("📲 Universal Mobile Downloader")
st.write("TikTok, Instagram, aur YouTube videos download karein.")

# QUALITY SELECTION OPTION
quality_choice = st.selectbox(
    "⚙️ Select Video Quality:",
    ["Best Quality (HD/1080p)", "Normal Quality (SD/720p)", "Low Data Mode (360p)"]
)

url = st.text_input("Paste Video Link Here:", placeholder="https://...")

if st.button("DOWNLOAD NOW"):
    if url:
        try:
            with st.spinner("🚀 Premium bypass engine se video fetch ki ja rahi hai..."):
                timestamp = int(time.time())
                
                # Direct Rapid API that doesn't care about hosting blocks
                api_url = "https://api.cobalt.tools/api/json"
                payload = {
                    "url": url,
                    "videoQuality": "1080",
                    "isAudioOnly": False
                }
                headers = {
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                }
                
                response = requests.post(api_url, json=payload, headers=headers, timeout=15)
                
                if response.status_code == 200:
                    data = response.json()
                    video_url = data.get("url")
                    
                    if video_url:
                        video_bytes = requests.get(video_url, timeout=15).content
                        
                        st.success("✨ Video successfully fetched!")
                        st.write(f"🎯 Download Mode: **{quality_choice}**")
                        
                        # Video Player
                        st.video(video_bytes)
                        
                        # SAVE TO GALLERY BUTTON
                        st.download_button(
                            label="📥 Save to Device / Gallery",
                            data=video_bytes,
                            file_name=f"download_{timestamp}.mp4",
                            mime="video/mp4"
                        )
                    else:
                        st.error("Is video ka data platform se nahi mil saka. Please link check karein.")
                else:
                    st.error("Server filter refresh ho raha hai. Ek baar page reload karke check karein.")

        except Exception as e:
            st.error("Network temporary busy. Please wait 1 minute and try again.")
    else:
        st.warning("Pehle koi link paste karein!")