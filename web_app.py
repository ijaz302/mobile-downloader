import streamlit as st
import requests
import google.generativeai as genai

# --- API CONFIG ---
# Secrets mein key daalna sabse best hai
API_KEY = st.secrets.get("GOOGLE_API_KEY", "PASTE_YOUR_API_KEY_HERE")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.0-pro')

# Custom Design
st.markdown("""
    <style>
    .big-font { font-size: 20px !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 TikTok Video Downloader")
st.markdown("Download TikTok videos in HD, without watermark.")

# --- Main Downloader ---
url = st.text_input("Paste TikTok link here:", placeholder="https://www.tiktok.com/...")
if st.button("Download Now"):
    if url:
        with st.spinner('Fetching your video...'):
            api = f"https://www.tikwm.com/api/?url={url}"
            res = requests.get(api).json()
            if res.get('code') == 0:
                data = res['data']
                st.video(data.get('play'))
                st.markdown(f'[⬇️ Click here to Download]({data.get("play")})')
            else:
                st.error("Invalid URL. Please check the link.")

st.markdown("---")

# --- AI Beauty Expert Section ---
with st.expander("💄 Need Beauty/Makeup Advice?"):
    user_q = st.text_input("Ask our Beauty AI:")
    if st.button("Ask AI"):
        if user_q:
            response = model.generate_content(f"You are a beauty expert. Answer: {user_q}")
            st.write(response.text)

# --- Professional FAQ Section (As per your video) ---
st.subheader("Frequently Asked Questions")
with st.expander("How to download TikTok video without watermark?"):
    st.write("1. Copy the link from TikTok app. 2. Paste it in the input box above. 3. Click Download.")
with st.expander("Is it free?"):
    st.write("Yes, our downloader is completely free and unlimited.")
