import streamlit as st
import requests
import google.generativeai as genai

# --- API CONFIG ---
# Streamlit secrets se key utha rahe hain
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# Model configuration
model = genai.GenerativeModel('gemini-pro')

# --- Page Setup ---
st.set_page_config(page_title="AI Beauty & Downloader", layout="centered")
st.title("✨ TikTok Downloader & AI Beauty")

tab1, tab2 = st.tabs(["🚀 Downloader", "💄 Beauty AI"])

with tab1:
    url = st.text_input("Paste TikTok link:")
    if st.button("Download"):
        if url:
            api = f"https://www.tikwm.com/api/?url={url}"
            res = requests.get(api).json()
            if res.get('code') == 0:
                st.video(res['data']['play'])
            else:
                st.error("Invalid URL")

with tab2:
    q = st.text_input("Ask Beauty AI:")
    if st.button("Ask"):
        if q:
            # Simple response call
            response = model.generate_content(f"You are a beauty expert. Answer: {q}")
            st.write(response.text)
