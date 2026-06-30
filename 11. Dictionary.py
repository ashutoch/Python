
#! Dictionary: Like a real life dictionary... have key-value pairs

#? example
# student = {
#     "name" : "Ashu",
#     'age' : 6,
#     'course' : "AI ML"
# }

# print(student)
# print(type(student))


#? Creating an empty dictionary

# dict = {}


#! How to access the values

# student = {
#     "name" : "Ashu",
#     'age' : 6,
#     'course' : "AI ML"
# }

# print(student['name'])

# print(student.get('age'))



#! Avoid keyerror: a key is not in the dictionary but we are trying to access it

# print(student.get('phone'))     # gives output as none indicating that the key doesnt exists
# if we use the normal way to access it it will show error

# print(student.get('phone', 'not found'))        # now the output will be not found insted of none 



#! Adding and updating a new key
# student = {
#     "name" : "Ashu",
#     'age' : 6,
#     'course' : "AI ML"
# }

# adding a new key
# student['blood group'] = 'B +ve'
# print(student)

# updating a key's value
# student['course'] = 'AI/ML Automations'
# print(student)


#! Removing items from key
# student = {
#     "name" : "Ashu",
#     'age' : 6,
#     'course' : "AI ML"
# }

#? remove by key

# student.pop('age')
# print(student)

#? removeby delete method

# del student['age']
# print(student)

#? clear all items (item = key + value pair) 

# student.clear()
# print(student)


#! Dictionary Methods

# person = {
#     'hobby' : 'sketching',
#     'state' : 'odisha',
#     'university' : 'ABC'
# }

# Dictionary key
# print(person.keys())

# Dictionary values
# print(person.values())

# Dictionary items
# print(person.items())


#! Loop through a dictionary

# for key, value in person.items():
#     print(key, ": ",value)


#! Nested Dictionaries

# student = {
#     '101' : {
#         'name' : "ashu",
#         'age' : 6
#     },
#     '102' : {
#         'name' : "ashutosh",
#         'age' : 5
#     }
# }

# print(student)
# print(student['101'])
# print(student['101']['name'])


#! Dictionary Comprehension (square)
# square of numbers

# squares = {
#     x: x**2 for x in range(5)
# }

# print(squares)


#! Merging Dictionaries
# d1 = {
#     'a' : 1,
#     'b' : 2
# }

# d2 = {
#     'b' : 6,
#     'c' : 3,
#     'd' : 4
# }

# merged = {**d1, **d2}
# print(merged)
#? it takes the values of the latter dictionary and updates the value for the key if both the dictionaries have the same key name


#! Counter for frequency

# from collections import Counter

# data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# counter = Counter(data)
# print(counter)
# print(counter['apple'])
# print(counter['banana'])


#! Voice and Chat Assistant (Chat to Voice Assistant)


#? Importing necessary libraries

import pyttsx3
from datetime import datetime

#? Initialize the text to speech engine

#? Define a function to speak text

def speak(text):
    print("🤖 Jarvis:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine


#? Greet
print("\n\nJarvis: Hello! I am a python AI assistant bot... Type 'exit' to end\n")

#? Starting a chat loop

while True:
    user_input = input("👤 You: ").lower()

    if user_input == 'exit':
        speak("""Hope i was able to help...
        Good bye sir!\n""")
        break

    elif 'hello' in user_input or 'hi' in user_input:
        speak("Hey there! I am Jarvis, how may I assist you today good sir?\n")

    elif 'how are you' in user_input:
        speak("Feeling like a new born...\n A bit cranky and wobbly as well!!\n")

    elif 'name' in user_input:
        speak("My name is Jarvis, your python AI assistant...\n")

    elif 'time' in user_input:
        current_time = datetime.now().strftime("%H:%M:%S\n")
        speak(current_time)

    elif 'calculate' in user_input:
        try:
            result = eval(user_input.replace("calculate", ""))
            speak(f"The result is: {result}\n")
        except:
            speak("Sorry i am unable to calculate that right now\n")

    else:
        speak("I didn't understand that. Can you try again?\n")