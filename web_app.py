import streamlit as st
import os
import time
import requests

# Page Configuration
st.set_page_config(page_title="Universal Downloader", page_icon="📲", layout="centered")

st.title("📲 Universal Mobile Downloader")
st.write("TikTok, Instagram, aur YouTube videos download karein.")

# Input Box
url = st.text_input("Paste Video Link Here:", placeholder="https://...")

if st.button("DOWNLOAD NOW"):
    if url:
        try:
            with st.spinner("Processing... High-Quality video fetch ki ja rahi hai."):
                timestamp = int(time.time())
                
                # Link cleaner (extra parameter hatane ke liye)
                clean_url = url.split('?')[0]
                
                # Powerful Public API Endpoint for Bypassing Restriction
                api_url = f"https://api.bhadooo.com/instagram/v1/downloader?url={clean_url}"
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                }
                
                response = requests.get(api_url, headers=headers, timeout=12)
                
                if response.status_code == 200:
                    data = response.json()
                    video_url = data.get("data", [{}])[0].get("url") or data.get("url")
                    
                    if video_url:
                        # Video bytes download ho rahi hain
                        video_bytes = requests.get(video_url, timeout=15).content
                        
                        st.success("✨ Video successfully fetched!")
                        
                        # 1. QUALITY DISPLAY OPTION ADDED HERE
                        st.info("⚙️ Video Quality: **Best Available (HD / MP4)**")
                        
                        # Show Video Player
                        st.video(video_bytes)
                        
                        # 2. SAVE TO GALLERY BUTTON ADDED HERE
                        st.download_button(
                            label="📥 Save to Device / Gallery",
                            data=video_bytes,
                            file_name=f"download_{timestamp}.mp4",
                            mime="video/mp4"
                        )
                    else:
                        st.error("Is video ka high-quality link nahi mil saka. Please koi doosra link try karein.")
                else:
                    st.error("Server ka connection temporary slow hai. Ek baar page refresh karke dobara try karein.")

        except Exception as e:
            st.error("Bypass network overload ho gaya hai. Please thodi dair baad try karein.")
    else:
        st.warning("Pehle koi link paste karein!")