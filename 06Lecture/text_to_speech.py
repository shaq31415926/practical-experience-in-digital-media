from gtts import gTTS
# Reference: https://reintech.io/blog/how-to-create-a-speech-synthesis-system-with-python


def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    filename = "audio/speech.mp3"
    tts.save(filename)


#text = input("What text would you like to convert?:")
text = """Welcome to the first streamlit-based Snake Game! Explore the captivating universe of Snake, where the pursuit of high scores and the avoidance of collisions create an engaging and memorable gaming experience. With intuitive controls and beautiful graphics, this version of Snake will keep you entertained for hours."""
text_to_speech(text)
print("Your text has been converted")
