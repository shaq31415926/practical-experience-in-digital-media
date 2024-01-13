import streamlit as st


options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'])


for n, g in enumerate(options):
    # replace the green, yellow etc with anime categories and corresponding
    if options[n] == "Green":
        options[n] = "1"
    if options[n] == "Yellow":
        options[n] = "2"
    if options[n] == "Red":
        options[n] = "3"
    if options[n] == "Blue":
        options[n] = "4"

genre_choice = tuple(options)
print(genre_choice)