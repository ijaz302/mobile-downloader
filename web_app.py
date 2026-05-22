import streamlit as st
import requests
import google.generativeai as genai

# --- API CONFIG ---
# Yahan apni API Key daalein
API_KEY = st.secrets.get("GOOGLE_API_KEY", "AIzaSyARMwXJJKN0lWceW4RZVjBsqYDaJnTXAKY")

genai.configure(api_key=API_KEY)

# Sabse stable model call
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="AI Beauty & Downloader", layout="centered")
st.title("✨ AI Beauty Assistant & Downloader")

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
                st.markdown(f'[⬇️ Download]({data.get("play")})')
            else:
                st.error("Invalid URL.")

with tab2:
    st.info("Ask me about makeup or skincare!")
    user_q = st.text_input("Question:")
    if st.button("Get AI Advice"):
        if user_q:
            with st.spinner('Thinking...'):
                try:
                    # Model list check karne ki zaroorat nahi, seedha call
                    response = model.generate_content(f"Answer as a beauty expert: {user_q}")
                    st.write(response.text)
                except Exception as e:
                    # Agar abhi bhi error aaye, toh error message saaf dikhega
                    st.error(f"Issue: {e}")
