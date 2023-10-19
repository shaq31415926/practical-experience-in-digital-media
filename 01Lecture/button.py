import streamlit as st

# add the title for the app
st.title("Creating buttons")

# create a count variable that will keep track of how many times the user clicks on the button
if 'count' not in st.session_state:
    st.session_state.count = 0


# this is the definiton that will add one to the counter every time the user clicks on it
def increment_counter():
    st.session_state.count += 1


# when the user clicks on the button the increment_counter definition will be activated
st.button("Click Here",
          help="Click here to see the emoji change",
          on_click=increment_counter)

print(st.session_state.count)
# if the count is an even number we write a happy emoji
if st.session_state.count % 2 == 0:
    st.write(":joy:")
# otherwise print a sad emoji
else:
    st.write(":cry:")
