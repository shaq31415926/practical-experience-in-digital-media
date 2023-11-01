# Reference: https://github.com/prateekralhan/qrcode-generator-streamlit/blob/main/app.py

import os
import streamlit as st
import segno
import time
from datetime import datetime
import base64


# create a title
st.title("✨QR Code Generator 🚀")
url = st.text_input("Enter your URL please 👇")

# create a timestamp to store and read your QR codes
current_ts = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

# create a def that wil take the url and generate an animated qr code
def generate_animated_qrcode():
    print("to be updated")


if url is not None and url != "":
    with st.spinner('Generating QR Code... 💫'):
        time.sleep(2.5)
    generate_animated_qrcode()

    # open the animated qr code image and load it to your streamlit app
    # reference: https://discuss.streamlit.io/t/how-to-show-local-gif-image/3408/3
    #file_ = open("images/my_animated_qrcode_working.gif", "rb")
    file_ = open("https://github.com/shaq31415926/practical-experience-in-digital-media/blob/main/02Lecture/images/my_animated_qrcode_working.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="gif">',
        unsafe_allow_html=True,
    )