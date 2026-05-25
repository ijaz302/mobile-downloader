import streamlit as st
import requests

# Layout: Wide aur clean
st.set_page_config(page_title="TikTok Downloader", layout="wide")

# CSS: Hard-coded colors for a professional look (White Cards on Grey Background)
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; }
    .main-card {
        background-color: white !important;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        text-align: center;
        color: #333;
    }
    h1 { color: #333 !important; }
    </style>
""", unsafe_allow_html=True)

# Main Container
st.markdown("<div class='main-card'>", unsafe_allow_html=True)
st.title("🎬 TikTok Video Downloader")
st.write("Download HD TikTok videos without watermark.")

url = st.text_input("", placeholder="Paste TikTok link here...")

# Button styling fix
if st.button("Download Now"):
    if url:
        with st.spinner('Fetching...'):
            api = f"https://www.tikwm.com/api/?url={url}"
            res = requests.get(api).json()
            if res.get('code') == 0:
                st.video(res['data']['play'])
            else:
                st.error("Invalid URL!")
st.markdown("</div>", unsafe_allow_html=True)

# FAQ Section
st.write("---")
st.subheader("Frequently Asked Questions")
with st.expander("Is this free?"):
    st.write("Yes, 100% free.")
with st.expander("How to use?"):
    st.write("Copy link, paste, click download.")
