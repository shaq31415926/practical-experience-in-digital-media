import streamlit as st
import time
import segno
from datetime import datetime
from PIL import Image

# code to config the page
st.set_page_config(
    page_title="QR Code Generator",
    page_icon="💫"
)

main_image = Image.open("images/main_banner.png")
st.image(main_image)

# code to add a title
st.title("QR Code Generator 🚀")

# add a text box
url = st.text_input("Enter your URL please 👇")

# create a timestamp variable
current_ts = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")


def generate_qrcode(url, current_ts):
    qrcode = segno.make_qr(url)
    qrcode.save(f"images/qrcode-{current_ts}.png",
                scale=5)


# if url exists
if url is not None and url != "":
    # create a spinner which adds some suspense
    with st.spinner("Generating QR Code... 💫"):
        time.sleep(1.5)
    generate_qrcode(url, current_ts)

    image = Image.open(f"images/qrcode-{current_ts}.png")

    st.image(image,
             caption="Here is our QR Code :)",
             width=200)

# if no url, give user a warning
else:
    st.warning("⚠ Please enter your URL!")

# create a footer
st.markdown("<br><hr><center>Made by SHaq</a></center><hr>",
            unsafe_allow_html=True)