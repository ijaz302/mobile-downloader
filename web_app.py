import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="TikTok Downloader Pro - No Watermark", layout="centered")

# Custom CSS for Professional Look
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #ff4b4b; color: white; font-weight: bold; }
    .footer { text-align: center; margin-top: 50px; font-size: 12px; color: #888; }
    .download-btn { display: block; text-align: center; background: #28a745; color: white; 
                    padding: 15px; border-radius: 10px; text-decoration: none; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🚀 TikTok Downloader Pro")
st.subheader("Fast, Secure & HD Video Downloader")

# URL Input
url = st.text_input("Paste your TikTok link here:")

if "video_data" not in st.session_state:
    st.session_state.video_data = None

# Action Logic
if st.button("Fetch & Download"):
    if url:
        with st.spinner('Preparing your high-quality video...'):
            try:
                api = f"https://www.tikwm.com/api/?url={url}"
                res = requests.get(api).json()
                if res.get('code') == 0:
                    st.session_state.video_data = res['data']
                else:
                    st.error("Invalid URL or Video not found.")
            except:
                st.error("Server error. Please try again.")

# Display Result
if st.session_state.video_data:
    data = st.session_state.video_data
    quality = st.radio("Select Quality:", ("Normal", "HD (High)"), horizontal=True)
    video_url = data.get('hdplay') if quality == "HD (High)" else data.get('play')
    
    st.video(video_url)
    st.markdown(f'<a href="{video_url}" target="_blank" class="download-btn">⬇️ Save to Gallery</a>', unsafe_allow_html=True)

# Footer & SEO Sections
st.markdown("---")
st.markdown("### How to use?")
st.info("1. Copy the TikTok link.\n2. Paste it in the box above.\n3. Click 'Fetch & Download'.\n4. Save it to your device.")

st.markdown("---")
st.markdown("""
    <div class="footer">
        <p>© 2026 TikTok Downloader Pro. All rights reserved.</p>
        <p>Disclaimer: This tool is not affiliated with TikTok. We do not host any videos.</p>
        <p>Contact: support@downloader.com | Privacy Policy</p>
    </div>
""", unsafe_allow_html=True)
