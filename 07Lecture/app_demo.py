import streamlit as st
from src.snake_game import snake_game


# set the page config info
st.set_page_config(
    page_title="My Snake Game",
    page_icon="🐍",
    layout="wide"
)

# create a placeholder variable
placeholder = st.empty()
credentials_check = False

# create the log in form
with placeholder.form("Login"):
    st.markdown("Enter your user information")
    user_name = st.text_input("Username", placeholder="Please enter your user name")
    password = st.text_input("Password", placeholder="Please enter your password", type="password")
    login_button = st.form_submit_button("Login")

    if login_button:
        credentials_check = True


if credentials_check == True:
    # delete all the form widgets we created
    placeholder.empty()
    # call the definition that launches the snake game
    snake_game()