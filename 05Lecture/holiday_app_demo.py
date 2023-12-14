import streamlit as st

# code to config the page
st.set_page_config(
    page_title="Holiday App",
    page_icon=":snowman:"
)

# heading
st.header("GOOD LUCK AND HAPPY HOLIDAYS", divider="rainbow")

# add an image
file_path = "https://github.com/shaq31415926/practical-experience-in-digital-media/blob/main/05Lecture/images/snowman.jpeg?raw=true"
st.image(file_path,
         #width=200,
         caption="IT'S A SNOWMAN")