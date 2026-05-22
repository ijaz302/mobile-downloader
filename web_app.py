import streamlit as st
import requests
import google.generativeai as genai

# --- API CONFIG ---
# Agar Secrets mein key nahi dali, to yahan apni API Key paste karein
API_KEY = st.secrets.get("GOOGLE_API_KEY", "AIzaSyCUdLxGuryJRVM9VCowN5z1Ua5ycXv1qT4")

genai.configure(api_key=API_KEY)

# Model configuration - hum 'gemini-1.5-flash' use kar rahe hain
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Page Setup ---
st.set_page_config(page_title="AI Beauty & Downloader", layout="centered")
st.title("✨ AI Beauty Assistant & Downloader")

tab1, tab2 = st.tabs(["🚀 TikTok Downloader", "💄 Ask Beauty AI"])

with tab1:
    url = st.text_input("Paste TikTok link:")
    if st.button("Fetch & Download"):
        if url:
            with st.spinner('Fetching...'):
                api = f"https://www.tikwm.com/api/?url={url}"
                res = requests.get(api).json()
                if res.get('code') == 0:
                    data = res['data']
                    st.video(data.get('play'))
                    st.markdown(f'[⬇️ Click here to Download]({data.get("play")})')
                else:
                    st.error("Invalid URL or Video not found.")

with tab2:
    st.info("Ask me about makeup, skincare, or beauty tips!")
    user_q = st.text_input("Ask a question:")
    if st.button("Get AI Advice"):
        if user_q:
            with st.spinner('AI is thinking...'):
                try:
                    # AI ko prompt de rahe hain
                    response = model.generate_content(f"You are a professional makeup and skincare expert. Please answer this: {user_q}")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"AI Error: {e}. Please check if your API Key has access to 'gemini-1.5-flash'.")
