import streamlit as st

st.title("Radio Buttons")

food_options = ["-",
                ":pizza:",
                ":hamburger:",
                ":ramen:",
                ":cake:",
                ":fries:",
                ":lollipop:"]

food = st.radio("What is your favourite food?",
         (food_options)
         )

for f in food_options:
    if food == f and f != "-":
        st.write(f"I love {f}")
