import segno
import streamlit as st
from datetime import datetime
import time
from PIL import Image


def generate_qrcode(url, current_ts):
    qrcode = segno.make_qr(url)
    qrcode.save(f"images/qrcode-{current_ts}.png",
                scale=5)


def generate_qrcode_page():
    # input box where the user can enter the text/url they want to encode
    url = st.text_input("Enter your URL please 👇")
    # create a timestamp variable
    current_ts = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

    # if url exists
    if url is not None and url != "":
        # create a spinner which adds some suspense
        with st.spinner("Generating QR Code... 💫"):
            time.sleep(1.5)
        # generates the qr code
        generate_qrcode(url, current_ts)

        # reads the qr code and places it on the app
        image = Image.open(f"images/qrcode-{current_ts}.png")
        st.image(image,
                 caption="Here is our QR Code :)",
                 width=200)

    # if no url, give user a warning
    else:
        st.warning("⚠ Please enter your URL!")