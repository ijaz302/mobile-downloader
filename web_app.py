import streamlit as st
import requests

# Layout Setup
st.set_page_config(page_title="TikTok Video Downloader", layout="centered")

# CSS for a professional look
st.markdown("""
    <style>
    .header { text-align: center; color: #333; }
    .nav { text-align: center; margin-bottom: 20px; }
    .footer { text-align: center; font-size: 12px; color: #777; margin-top: 50px; }
    </style>
""", unsafe_allow_html=True)

# Header Navigation
st.markdown("<div class='nav'>TikTok Downloader | Instagram Downloader | Twitter Downloader</div>", unsafe_allow_html=True)
st.markdown("<h1 class='header'>TikTok Video Downloader</h1>", unsafe_allow_html=True)

# Main Input
url = st.text_input("Insert a link here:", placeholder="Paste your TikTok link...")
if st.button("Download"):
    if url:
        api = f"https://www.tikwm.com/api/?url={url}"
        res = requests.get(api).json()
        if res.get('code') == 0:
            st.video(res['data']['play'])
        else:
            st.error("Invalid link!")

# Detailed Info Section (Jaisa video mein tha)
st.write("---")
st.subheader("How to download TikTok video without watermark?")
st.write("1. **Find a TT**: Open the TikTok app and find the video.")
st.write("2. **Copy the link**: Tap the Share button and select 'Copy link'.")
st.write("3. **Save TikTok**: Paste the link in the box above and click Download.")

# FAQ Section
st.subheader("Frequently Asked Questions")
with st.expander("Is TikTok download available in MP4 format?"):
    st.write("Yes, all videos are downloaded in high-quality MP4 format.")
with st.expander("Where are TikTok videos saved after downloading?"):
    st.write("Videos are saved in your device's default 'Downloads' folder.")

# Footer
st.markdown("<div class='footer'>© 2026 TikTok Video Downloader. All rights reserved.</div>", unsafe_allow_html=True)
