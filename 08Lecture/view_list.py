import streamlit as st

list = ["Bob", "Marley"]
code = []
font_colour = "#9c9d9f"
font_size = "20"

for i in list:
    code.append(f'<li style="font-size: {font_size}px; color:{font_colour}" align="justify">{i}</li>')

complete_code = "".join(code)
st.write(f'<ul>{complete_code}</ul>', unsafe_allow_html=True)
