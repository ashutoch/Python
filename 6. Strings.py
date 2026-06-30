
#1 Introduction to strings

# a = "hello" 
# a = 'hello'
a = """Multiline
Strings"""

# print(a)


#! Concatenation and Repetition

name = "Ashutosh"
# print(name * 4) #? Repetition

surname = "Meher"

# print (name + " " + surname)




#! String Methods
#? strip() - removes spaces form the beginning and the end

# text = "             HELLO BOI         "
# cleaned = text.strip()

# print(cleaned)


#? replace(old, new) - replaces part of a string with new string

# text = "Python seems easy for now"
# new_text = text.replace("easy", "awesome")

# print(new_text)


#? split(delimiter) - splits the string into a list

# text = "apple, banana, mango, guava" 
# items = text.split(",")

# print(items)
# print(type(items))


#? join(iterable) - joins list elements into a string

words = ['Python', 'is', 'fun']
sentence = " ".join(words) # can use any special character or symbol inplace of the whitespace
# print(sentence)


#? upper() & lower() - convert cases
# text = "Python"
# print("uppercase: ", text.upper())
# print("lowercase: ", text.lower())


#? title and capitalization - converts the first letter of any word
# text = "Python is powerful"
# print(text.title)


#? String Indexing and SLicing
# syntax for slicicng: s[start: end : step]

# a = "Python seems mazedaar"
# print(a[0])
# print(a[-1])

# print(a[1 : 3])
# print(a[ : 6])
# print(a[0 : ])
# print(a[ : : 2])


#? to print the dynamic (user given data) and simple text at the same time

# s = "and this is dynamic text"
# print(f"this is a simple text {s}")

#? Advance string manipulation  ASCII values: ord(), chr()

# ord() is used to find the ASCII value for characters

# print(ord("A"))
# print(ord("a"))

# chr() is used to convert the corresponding ASCII code into a character
# print(chr(65))

#? Lamda Use - capitalise the first letter of every word 

# words = ["python", "anaconda"]

# capitalise = list(map(lambda a: a.capitalize(), words))
# print(capitalise)


#? Palindrome or reverse string

# word = input("enter a word: ")
# if word == word[: :-1] :
#     print("Yes its a palindrome")

# else:
#     print("Not a palindrome")


#! Animate a string and show it in the terminal

# sys - here we use it to directly write the o/p to the console (sys.stdout.write())

# time - it allows us to pause the program using time.sleep() - this is what makes the typing effect possible here

# import sys
# import time

# text = "Welcome to your study table man 🥹"

# for char in text:
#     sys.stdout.write(char)
#     sys.stdout.flush()  # this flush line helps us to print the letters of the text 1 by 1
    
#     time.sleep(0.5)



#! Password strength checker

while True:
    password = input("Enter your password: ")
    length  = len(password) >= 8
    upper = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password) 
    special = any(char in "@$%&?" for char in password)

    if length and upper and digit and special:
        print("Strong Password")
    elif length and (upper or digit or special):
        print("Moderate Password")
    else:
        print("Try again with a stronger password")
