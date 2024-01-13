import streamlit as st
import requests, json
import random

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'])

def generate_genre(*genre_choice):
    payload = {"filter":"tv",
               "genres": genre_choice}   #decides what genres should be picked
    anime_url = "https://api.jikan.moe/v4/anime"
    r = requests.get(anime_url, params=payload).text   #searches for titles that fulfill the user choice
    sex = json.loads(r) #transforms into json

    #collects number of pages of chosen anime and randomly chooses 1
    pages = sex["pagination"]["last_visible_page"]
    rand_page = random.randint(1,pages)
    payload["page"] = rand_page
    x = requests.get(anime_url, params=payload).text
    sex3 = json.loads(x)

   # print(f"number of all pages: {pages}")
    #print(payload)
    print("_______________________")

    #prints all anime from randomly picked page
    num = 0
    title = sex3["data"][num]["title"]
    syn = sex3["data"][num]["synopsis"]
    img = sex3["data"][num]["images"]["webp"]["image_url"]

    return title, syn, img

# if user selects something
if options:
    # map the output to a key that the api can pick up
    for n, g in enumerate(options):
        # replace the green, yellow etc with anime categories and corresponding
        if options[n] == "Green":
            options[n] = "1"
        if options[n] == "Yellow":
            options[n] = "2"
        if options[n] == "Red":
            options[n] = "3"
        if options[n] == "Blue":
            options[n] = "28"

    # convert the list to a tuple
    genre_choice = tuple(options)
    # in your terminal, check if what is being selected is what you expect
    print(genre_choice)
    # call the generate genre definition and write the outputs
    title, syn, img = generate_genre(*genre_choice)
    st.write(title)
    st.write(syn)
    st.write(img)