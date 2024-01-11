import streamlit as st

# set the page config info
st.set_page_config(
    page_title="My Snake Game",
    page_icon="🐍")

tab1, tab2 = st.tabs(["Introduction", "The Game"])

with tab1:
    # create subheader for the sections
    st.subheader('| Intro')
    c1, c2 = st.columns(2)
    with c1:
        st.image("images/snake_cartoon.png")
    with c2:
        intro_text = """
        Welcome to the first streamlit-based Snake Game! Explore the captivating universe
        of Snake, where the pursuit of high scores and the avoidance of collisions 
        create an engaging and memorable gaming experience. With intuitive controls and 
        beautiful graphics, this version of Snake will keep you entertained for hours.
        """

        # if you want to adjust the size and colour of the font you have to use some html
        st.write(f'<p style="font-size: 14px; color:#9c9d9f">{intro_text}</p>',
                 unsafe_allow_html=True)

    st.subheader('| Instructions 🕹️')
    st.subheader('| Code')

with tab2:
    c1, c2, c3 = st.columns(3)
    with c2:
        st.image("https://media.giphy.com/media/VHOF8pfPZOt9p018zw/giphy.gif", width=400)


