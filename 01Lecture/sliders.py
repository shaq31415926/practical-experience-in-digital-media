import streamlit as st

# code to add a title
st.title("Creating sliders :smile:")

# code to add a slider
score = st.slider("Rate how much you love Python",
          min_value=0,
          max_value=10,
          # this is the value the user sees when the app is opened
          value=10
          )

if score >= 7:
    st.write("I :heart: Python")
elif score > 4 and score < 7:
    st.write("I am unsure about Python")
else:
    st.write(":cry:")

