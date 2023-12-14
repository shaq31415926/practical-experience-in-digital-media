import streamlit as st

# code to config the page
st.set_page_config(
    page_title="Holiday App",
    page_icon=":snowman:"
)

# create a count variable that will keep track of how many times the user clicks on the button
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter():
    st.session_state.count += 1


# heading
st.header("GOOD LUCK AND HAPPY HOLIDAYS", divider="rainbow")

st.write(":snowman:")


# add an image
#file_path = "images/snowman.jpeg"
file_path1 = "https://github.com/shaq31415926/practical-experience-in-digital-media/blob/main/05Lecture/images/snowman.jpeg?raw=true"
file_path2= "https://t4.ftcdn.net/jpg/03/25/99/83/360_F_325998355_QXTUKMnb5TuVVyHJmixC6Vk2L338XcJn.jpg"


images = [file_path1, file_path2]


def holiday_image():
    increment_counter()
    # if the count is an even number we place a sad snowman
    if st.session_state.count % 2 == 0:
        st.image(file_path2,
                # width=200,
                caption="IT'S A SAD SNOWMAN")

    # otherwise place a happy snowman image
    else:
        st.image(file_path1,
                # width=200,
                caption="IT'S A HAPPY SNOWMAN")


# add a button
st.button("Click here",
          help="Click here for your holiday image",
          on_click=holiday_image)