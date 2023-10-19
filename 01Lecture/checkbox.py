import streamlit as st

st.title("Check boxes")

opt1 = st.checkbox("Option 1")
opt2 = st.checkbox("Option 2")
opt3 = st.checkbox("Option 3")
opt4 = st.checkbox("Option 4")
opt5 = st.checkbox("Option 5")

if opt1:
    st.write("You selected Option 1")
if opt2:
    st.write("You selected Option 2")
if opt3:
    st.write("You selected Option 3")
if opt4:
    st.write("You selected Option 4")
if opt5:
    st.write("You selected Option 5")

if opt1 and opt2 and opt3 and opt4 and opt5:
    st.write("YOU SELECTED EVERYTHING!!")



