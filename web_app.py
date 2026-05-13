import streamlit as st
import yt_dlp
import os
import time

# Page ki basic settings
st.set_page_config(page_title="Universal Downloader", page_icon="📲", layout="centered")

# Custom CSS taake app achi dikhay
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📲 Universal Mobile Downloader")
st.write("TikTok, Instagram, aur YouTube videos download karein.")

# User se link lena
url = st.text_input("Paste Video Link Here:", placeholder="https://...")

# Quality select karne ka option
quality = st.selectbox("Select Video Quality:", ["Best Quality", "Small Size"])

if st.button("DOWNLOAD NOW"):
    if url:
        try:
            with st.spinner("Processing... Is mein aik minute lag sakta hai."):
                
                # Har video ka bilkul alag naam banane ke liye
                timestamp = int(time.time())
                unique_filename = f"video_{timestamp}.mp4"
                
                # yt-dlp ki khas settings (Security block se bachne ke liye)
                ydl_opts = {
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                    'outtmpl': unique_filename,
                    'quiet': True,
                    'no_warnings': True,
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                    # Agar link Instagram/TikTok ka ho to ye headers madad karte hain
                    'http_headers': {
                        'Referer': 'https://www.google.com/',
                    }
                }

                # Video download karna
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                # Check karna ke file bani hai ya nahi
                if os.path.exists(unique_filename):
                    with open(unique_filename, "rb") as f:
                        video_bytes = f.read()
                        
                        # Video player dikhana
                        st.video(video_bytes)
                        
                        # Download button
                        st.download_button(
                            label="📥 Save to Device / Gallery",
                            data=video_bytes,
                            file_name=f"download_{timestamp}.mp4",
                            mime="video/mp4"
                        )
                    
                    # Download ke baad server se file delete karna taake memory full na ho
                    os.remove(unique_filename)
                else:
                    st.error("File download nahi ho saki. Dobara koshish karein.")

        except Exception as e:
            st.error("Security Block! TikTok/Instagram ne request rok di hai. Thori dair baad dobara koshish karein ya link check karein.")
    else:
        st.warning("Pehle koi link paste karein!")

st.info("Note: Agar video display nahi ho rahi, to 'Save to Device' button par click karke direct download kar lein.")
