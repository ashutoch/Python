
#! Tuples: ordered, immutable collection in python. Once created, you can't modify a tuple. Commonly used to store a collection of items that shouldn't change

# myTuple = ('apple', 'banana', 'grapes')
# print(myTuple)
# print(type(myTuple))


# single_item = ('mouse')
# print(type(single_item))  #? it shows it as a string. we need to add just 1 extra comma in it to make it into a tuple

# single_item = ('mouse',)
# print(type(single_item))


# list = ['laptop', 'mouse', 'keyboard']
# print(list)
# list[2] = 'pendrive'
# print(list)


#! slicing
# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# print(numbers[ 1 : 4 ])
# print(numbers[ : : 2 ])
# print(numbers[ : : -1 ])


#! Looping in a tuple

# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# for item in numbers:
#     print(item)



#! Packing and Unpacking
# packed_tuple = ('apple', 'banana', 'grapes')  
#? packing means putting multiple values into a tuple
# print(packed_tuple)

# item1, item2, item3 = packed_tuple
# print(item1)
# print(item2)
# print(item3)
#? unpacking assigns values from the tuples into individual variables


#! Methods
# tuple = ('apple', 'banana', 'grapes', 'apple', 'apple')  
# print(len(tuple))

# print(tuple.count('apple'))

# print(tuple.index('grapes'))


#! Convert Tuple to a List
#? as a tuple can't be modified

# colors = ('red', 'green', 'blue', 'white')

# color_list = list(colors)
# print (color_list)

# color_list.append('yellow')
# print(color_list)

# colors = tuple(color_list)
# print(colors)



#! Sorting
# pairs = [(1, 2), (0, 2), (5, 6), (5, 8), (0, 9), (1, 2, 5)]

# print(sorted(pairs))


#! Test to find out the highest among the given

# def topper(students):
#     highest_avg = 0
#     topper = ""
    
#     for name, marks in students:
#         avg = sum(marks) / len(marks)
        
#         if avg > highest_avg:
#             highest_avg = avg
#             topper = name
        
#         else:
#             name = "none"
    
#     return topper, highest_avg

# students = [
#     ("Ashu", [50, 60, 10]),
#     ("Ashutosh", [70, 80, 80]),
#     ("Ash", [90, 80, 80])
# ]

# print(topper(students))



#! Voice to PDF Item Report Generator
#? we will speak and it will record and understand our voice and make reports accordingly

#? Things to install first
# SpeechRegonition and pyaudio

#? Import those libraries
import speech_recognition as sr
from reportlab.pdfgen import canvas
# from word2number import w2n  # in case the voice recognition doesnt understand the number that you are speaking


#? Create Recognizer and Item Storage
r = sr.Recognizer()
items = []


#? Define Listen function
# with sr.Microphone() opens the microphone to listen
# r.listen(source) records the audio
# then we pass it to google's speech recognizer which converts it into text

def listen():
    with sr.Microphone() as source:
        print("🎤Speak (say 'exit' to finish)...")
        audio = r.listen(source)
    
    try: 
        return r.recognize_google(audio).strip()
    except:
        return ""



#? Keep listening till the user says exit

while True:
    text = listen()
    if not text:
        continue
    elif text.lower() == "exit":
        break

#? Extract Item Name and Price

    words = text.split()
    price = ""

    for w in words:
        if w.replace('.','').isdigit():
            price = w
            break
        
        # if not price:   # if spoken in words
        #     try:
        #         price = str(w2n.word_to_num(text))
        #     except:
        #         price = ""


#? Clean the item name

    item_name = "".join(w for w in words if not w.replace('.', '').isdigit() and w.lower() != 'rs'.capitalize())

#? Store items in the list
    if price:
        items.append((item_name, price))
        print(f"Added: {item_name}      Rs {price}")
    else:
        print("Repeat again and say item with price")



# #? Generate the PDF Report
# c = canvas.Canvas("Items_Report.pdf")

# #? Title
# c.setFont("Helvetica-Bold", 20)
# c.drawString(200, 800, "Item Report")

# #? Divider line
# c.line(50, 790, 550, 790)

# #? Items list
# c.setFont("Helvetica", 12)
# y = 770  # Start BELOW the title

# for i, (name, price) in enumerate(items, 1):
#     c.drawString(50, y, f"{i}.   {name} ------------- Rs {price}")
#     y -= 30  # More spacing between items

# c.save()
# print("Report PDF is Saved: Items_Report.pdf")



#? Generate the PDF Report
page_width = 595  # A4 width in points

c = canvas.Canvas("Items_Report.pdf")

# Title - centered
c.setFont("Helvetica-Bold", 20)
title = "Item Report"
title_width = c.stringWidth(title, "Helvetica-Bold", 20)
c.drawString((page_width - title_width) / 2, 800, title)

# Divider line
c.line(50, 790, 545, 790)

# Items list
c.setFont("Helvetica", 12)
y = 760

for i, (name, price) in enumerate(items, 1):
    name = name.strip().title()          # Capitalize each word
    c.drawString(50, y, f"{i}.")         # Number
    c.drawString(75, y, name)            # Item name (fixed column)
    c.drawString(300, y, f"Rs {price}")  # Price (fixed column)
    y -= 30

c.save()
print("Report PDF is Saved: Items_Report.pdf")