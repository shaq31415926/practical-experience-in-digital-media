import streamlit as st

# this will create a title with a laughing emoji in the streamlit app
st.title("Hello World :smile:")
# creates a horizontal line
st.write("---")

# code to add a header
st.header("This is a header")

# code to add a subheader
st.subheader("This is a subheader")

# you can add markdows to bold text
st.markdown("This is **really important**")
# you can add markdows to make your text in italics
st.markdown("This is really *important*")

code = """
def hello():
    print("hello")
"""

st.code(code, language="python")

st.latex("(a+b)2 + (a+b)^2 + 2*a*b")






# for a complete list of emojis: https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/gallery/emojis/emojis.py

