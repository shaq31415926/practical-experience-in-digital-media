import streamlit as st
import requests

# code to config the page
st.set_page_config(
    page_title="Cat App",
    page_icon=":cat:"
)

st.header("WELCOME TO MY :cat: APP", divider='rainbow')


def get_content():
    """Access the API and get the image URL"""
    contents = requests.get('https://cataas.com//cat')
    # contents = requests.get('https://cataas.com//cat/gif')
    return contents.content

# 03Lecture/images/main_banner.png
# https://github.com/shaq31415926/practical-experience-in-digital-media/blob/main/03Lecture/images/main_banner.png
#


def place_cat_image():
    """Place the cat image from the cataas.com API"""
    #cat_image = get_content()
    #cat_image = "https://raw.githubusercontent.com/shaq31415926/practical-experience-in-digital-media/blob/main/03Lecture/images/main_banner.png"
    cat_image = "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/other/dungeon_crawler.png"
    st.image(cat_image, width=200)


# add a button
st.button("Click here",
          help="Click to get a cat image",
          on_click=place_cat_image)
