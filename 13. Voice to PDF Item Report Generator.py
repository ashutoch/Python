
#! Voice to PDF Item Report Generator

import SpeechRecognition as sr
from reportlab.pdfgen import canvas    #? for styling
from word2number import w2n  #? in case the voice recognition doesnt understand the number that you are speaking

# Create recognizer and Item Storage

r = sr.Recognizer()
items = []      # Empty list to store the item names and prices

# Define the listen function

def listen():
    with sr.Microphone() as source:
        print("🎤Speak (say 'exit' to finish)...")
        audio = r.listen(source)    #? Stores everything the microphone has listened to 
    
    try:
        return r.recognize_google(audio).strip()    #? pass it to google recognizer to actually understand the things and strip all the unnecessary sounds
    except:
        return ""   #? if its unable to understand or if it ccouldn't properly hear what we are saying then it will take an empty string and rerun the code instead of showing errors


# Keep listening until user says exit

while True:
    text = listen()
    if not text:
        continue    #? if the text is empty then continue instead of showing error
    
    elif text.lower() == "exit":
        break

# Extract Item Name and Price

words = text.split()
price = ""