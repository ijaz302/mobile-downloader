import streamlit as st
import requests
import google.generativeai as genai

# --- API CONFIG ---
# Hum pehle Secrets check karenge, agar nahi milegi to hum direct key use karenge
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    api_key = "AIzaSyCUdLxGuryJRVM9VCowN5z1Ua5ycXv1qT4" # Agar aapne Secrets mein key nahi dali to yahan paste karein

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash') # 'gemini-1.5-flash' zyada stable hai

# --- Page Setup ---
st.set_page_config(page_title="AI Beauty & Downloader", layout="centered")

st.title("✨ AI Beauty Assistant & Downloader")

# --- TABS ---
tab1, tab2 = st.tabs(["🚀 TikTok Downloader", "💄 Ask Beauty AI"])

with tab1:
    url = st.text_input("Paste TikTok link:")
    if st.button("Fetch & Download"):
        if url:
            api = f"https://www.tikwm.com/api/?url={url}"
            res = requests.get(api).json()
            if res.get('code') == 0:
                data = res['data']
                st.video(data.get('play'))
                st.markdown(f'[⬇️ Click here to Download]({data.get("play")})')
            else:
                st.error("Invalid URL.")

with tab2:
    st.info("Ask me about makeup or skincare!")
    user_q = st.text_input("Your question:")
    if st.button("Get AI Advice"):
        if user_q:
            with st.spinner('AI is thinking...'):
                try:
                    response = model.generate_content(f"You are a beauty expert. Answer: {user_q}")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
