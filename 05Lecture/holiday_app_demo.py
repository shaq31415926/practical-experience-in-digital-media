import streamlit as st
import time

# code to config the page
st.set_page_config(
    page_title="Holiday App",
    page_icon=":snowman:"
)

# heading
st.header("GOOD LUCK AND HAPPY HOLIDAYS", divider="rainbow")

# add an image
#file_path = "images/snowman.jpeg"
file_path1 = "https://github.com/shaq31415926/practical-experience-in-digital-media/blob/main/05Lecture/images/snowman.jpeg?raw=true"
#file_path2="https://www.creativefabrica.com/wp-content/uploads/2020/10/26/Snowman-Christmas-Vector-Illustration-Graphics-6284110-1-1-580x431.jpg"

st.image(file_path1,
         #width=200,
         caption="IT'S A SNOWMAN")