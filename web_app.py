import streamlit as st
import requests
import google.generativeai as genai

# --- API CONFIG ---
# Apni API Key yahan quotes ke andar paste karein
GOOGLE_API_KEY = "AIzaSyCUdLxGuryJRVM9VCowN5z1Ua5ycXv1qT4"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# --- Page Setup ---
st.set_page_config(page_title="AI Beauty & Downloader", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; background-color: #ff4b4b; color: white; font-weight: bold; }
    .download-btn { display: block; text-align: center; background: #28a745; color: white; padding: 15px; border-radius: 10px; text-decoration: none; font-weight: bold; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("✨ AI Beauty Assistant & Downloader")

# --- TABS FOR UI ---
tab1, tab2 = st.tabs(["🚀 TikTok Downloader", "💄 Ask Beauty AI"])

with tab1:
    st.subheader("Fast & Watermark-Free Downloader")
    url = st.text_input("Paste your TikTok link here:")
    
    if "video_data" not in st.session_state:
        st.session_state.video_data = None

    if st.button("Fetch & Download"):
        if url:
            with st.spinner('Fetching video...'):
                try:
                    api = f"https://www.tikwm.com/api/?url={url}"
                    res = requests.get(api).json()
                    if res.get('code') == 0:
                        st.session_state.video_data = res['data']
                    else:
                        st.error("Invalid URL or Video not found.")
                except:
                    st.error("Server error. Please try again.")

    if st.session_state.video_data:
        data = st.session_state.video_data
        video_url = data.get('play')
        st.video(video_url)
        st.markdown(f'<a href="{video_url}" target="_blank" class="download-btn">⬇️ Save to Gallery</a>', unsafe_allow_html=True)

with tab2:
    st.subheader("Your Personal Beauty Expert")
    st.info("I am your AI Beauty Assistant! Ask me about makeup, skincare, or trending beauty tips.")
    
    user_q = st.text_input("Ask a beauty question:")
    if st.button("Get AI Advice"):
        if user_q:
            with st.spinner('Thinking...'):
                prompt = f"You are a professional beauty and makeup expert. Answer the following question in a friendly and helpful way: {user_q}. Also, suggest a common makeup product category if relevant to the tip."
                response = model.generate_content(prompt)
                st.write(response.text)
        else:
            st.warning("Please enter a question first!")

# --- Footer ---
st.markdown("---")
st.caption("© 2026 AI Beauty Assistant | Powered by Google Gemini")
