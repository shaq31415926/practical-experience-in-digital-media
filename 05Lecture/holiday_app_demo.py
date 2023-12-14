import streamlit as st

# code to config the page
st.set_page_config(
    page_title="Holiday App",
    page_icon=":snowman:"
)

# heading
st.header("GOOD LUCK AND HAPPY HOLIDAYS", divider="rainbow")

# add an image
st.image("images/snowman.jpeg",
         #width=200,
         caption="IT'S A SNOWMAN")