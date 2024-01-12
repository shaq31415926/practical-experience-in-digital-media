import streamlit as st
from snake_game import snake_game
from helpers import connect_to_deta, fetch_data

# set the page config info
st.set_page_config(
    page_title="My Snake Game",
    page_icon="🐍")

placeholder = st.empty()  # this is to remove the login page
check_credentials = False

# create database in deta
db = connect_to_deta(db_name="snake_db")
# create the structure of the base - you can delete this later
# db.insert({"user_name": "", "password": ""})


# create a login page
with placeholder.form("login"):
    st.markdown(f'<p style="font-size: 20px; color:grey">Hello! Please enter your log in info.'
                f'<br>If this is your first time on my app then please create a username and password.</p>',
                unsafe_allow_html=True)
    user_name = st.text_input('Username', placeholder="Please create or enter a user name").lower()
    password = st.text_input("Password", placeholder="Please create or enter a password", type="password")
    login_button = st.form_submit_button("Login")

    if login_button:
        # give warnings if user does not enter anything
        # however there are much better ways to do the authentication, and there is also a library
        if len(user_name) == 0 and len(password) == 0:
            st.warning('Please enter username and password', icon="⚠️")
        elif len(user_name) == 0:
            st.warning('Please enter username', icon="⚠️")
        elif len(password) == 0:
            st.warning('Please enter password', icon="⚠️")
        # only if user enters username and password do we get to this stage
        else:
            # check if user name exists
            # to validate the uniqueness of the user_name
            # use the fetch function to fetch and
            user_data = fetch_data(db)
            user_names = list(user_data.user_name)

            # if user name is found then check the password
            if user_name in user_names:
                # check password
                registered_password = list(user_data[user_data["user_name"] == user_name]["password"])[0]

                if registered_password == password:
                    check_credentials = True
                else:
                    st.error('Please enter the CORRECT password', icon="⚠️")
            # else insert the user - however, could also add a user name validation step
            else:
                # to insert the data - use the insert function and pass in a dictionary
                db.insert({"user_name": user_name,
                           "password": password})
                check_credentials = True


# if credentials have been validated, enter the game
if check_credentials == True:
    placeholder.empty() # clear the form that was created
    snake_game()
