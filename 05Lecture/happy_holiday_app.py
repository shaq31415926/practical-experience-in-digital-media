import streamlit as st

# code to config the page
st.set_page_config(
    page_title="Happy Holiday App",
    page_icon=":snowman:"
)

st.header("HAPPY HOLIDAYS EVERYONE AND GOOD LUCK", divider='rainbow')

#image_file_path = "https://github.com/shaq31415926/practical-experience-in-digital-media/blob/main/05Lecture/images/snowman.jpeg?raw=true"
image_file_path = "images/snowman.jpeg"
st.image(image_file_path)

