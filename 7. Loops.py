
# Loops help you to repeat a block of code multiple times
# It is perfect for automation, data processing and building AI Systems

#? for loop range (start, stop, step)

# for i in range(10):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)


#! Real life example
# to send mail to a lot of person at the same time

# emails = ["a@gmail.com", "b@gmail.com", "c@gmail.com", "d@gmail.com"]

# for email in emails:
#     print("sent email to", email)


#? while loop

# i = 0
# while i < 5:
#     print(i)
#     i += 1


#? break

# for i in range(10):
#     if i == 5:
#         break
#     print(i)


#? continue

# for i in range (5):
#     if i == 2:
#         continue
#     print(i)


#? Nested loops

# for i in range(3):
#     for j in range(2):
#         print(f"i = {i}, j = {j}")


#? Loops with strings and list

# for char in "Python":
#     print(char)

# for item in [10, 8, 6, 4, 2, 0]:
#     print(item)


#? Strings

# text = "hippopotamus"
# for letter in text:
#     print(letter.upper())



#! Automation Bot to Rename Files:

# files = ["doe.jpg", "john.jpg", "loren.jpg"]

# for i, f in enumerate(files):  # enumerate stores the values of both the variables
# # here i is the index and f stores names of the files and enumerate works on both of them simultaneously
#     print(f"Renaming {f} to AM_{i}.jpg")


#? without enumerate

# files = ["doe.jpg", "john.jpg", "loren.jpg"]

# for i in range(len(files)):
#     f = files[i]
#     print(f"Renaming {f} to AM_{i}.jpg")



#! Resume Skill Extractor (NLP Automation)

# skills = ["python", 'ai', 'ml']
# resume = "Looking for a job for AI ML role with strong PYTHON skills".lower()

# for skill in skills:
#     if skill in resume:
#         print(f"Matched skill: {skill}")



#! AI auto directory creator

import os

folders = ["data", "models", "scripts", "notebooks", "output"]

project = input("Enter AI project name: ")

for folder in folders:
    path = os.path.join(project, folder)
    
    os.makedirs(path, exist_ok = True)
    
    print(f"Created: {path}")