import streamlit as st
import requests

# Page Config (SEO Title)
st.set_page_config(page_title="Free TikTok Video Downloader - No Watermark", layout="centered")

# SEO Header
st.title("🚀 TikTok Video Downloader - No Watermark")
st.write("Download your favorite TikTok videos in HD, MP4 format, and without any watermark. Fast, free, and secure.")

# Input Field
url = st.text_input("Paste your TikTok URL here:", placeholder="https://www.tiktok.com/@username/video/123456789")

if st.button("Download Now"):
    if url:
        with st.spinner('Fetching your video...'):
            try:
                api = f"https://www.tikwm.com/api/?url={url}"
                res = requests.get(api).json()
                if res.get('code') == 0:
                    st.video(res['data']['play'])
                    st.success("Success! Click on the video settings (three dots) to save.")
                else:
                    st.error("Invalid URL. Please check the link and try again.")
            except:
                st.error("Server error. Please try again.")

st.write("---")

# SEO Rich FAQ Section (Google likes this!)
st.header("Frequently Asked Questions (FAQs)")

faq_data = {
    "How to download TikTok videos without watermark?": "Copy the video link from TikTok, paste it in the box above, and click 'Download Now'.",
    "Is this TikTok Downloader free?": "Yes, our tool is 100% free and you can download unlimited videos.",
    "Do I need to install any app?": "No, this is a web-based tool. No installation is required.",
    "Does it work on iPhone?": "Yes, it works perfectly on iPhone, Android, and PC browsers.",
    "What quality are the videos?": "Videos are downloaded in the original resolution they were uploaded in.",
    "Is my data safe?": "We do not store any of your videos or personal information."
}

for question, answer in faq_data.items():
    with st.expander(question):
        st.write(answer)

# SEO Footer Content
st.write("---")
st.subheader("Why use our TikTok Downloader?")
st.write("""
Our downloader is the best solution for content creators and users who want to save TikToks 
without the watermark. Whether you are using Windows, macOS, Android, or iOS, our tool 
works seamlessly on all browsers. 
""")
