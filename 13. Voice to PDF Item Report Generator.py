
#! Voice to PDF Item Report Generator

import speech_recognition as sr
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

    for w in words:
        if w.replace('.', '').isdigit():    #? Checks if the data being checked is a digit or not
            price = w
            break
        
        if not price:
            try:
                price = str(w2n.word_to_num(text))  #? Helps to recognise the digits proerly
            except:
                price = ""

# Clean the item name

    item_name = " ".join(w for w in words if not w.replace('.', '').isdigit() and w.lower() != 'rs'.capitalize())   

# Store items in the list

    if price:
        items.append((item_name, price))
        print(f"Added: {item_name}      Rs {price}")
    else:
        print("Repeat again and say item with price")


# Generate PDF Report

c = canvas.Canvas("13.Items_Report.pdf")
c.setFont("Helvetica-Bold", 16)
c.drawString(200, 800, "Item Report")
c.setFont("Helvetica", 12)
y = 770

for i, (name, price) in enumerate(items, 1):
    name = name.strip().title()          # Capitalize each word
    c.drawString(50, y, f"{i}.")         # Number
    c.drawString(75, y, name)            # Item name (fixed column)
    c.drawString(300, y, f"Rs {price}")  # Price (fixed column)
    y -= 30

c.save()
print("Report PDF is Saved: Items_Report.pdf")