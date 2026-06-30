# REPL in python stands for Read -Eval - Print - LOOP
# Its like a live test lab for python where we can write one one line and check the output

# to start
# simple open terminal and type "python"  o/p >>> _
# after that simply write what you want and it will exectute it

# //? Examples
# 2 + 3
# 5 + 7
# print("Ashu")
# "Ashu" * 5 --- prints the string 5 times

# a = 5
# b = 10
# print (a + b)

# convert celsius to farenheit
# (celsius * 9/5) + 32

# find the length of a string
# len("Ashutosh")

# //! Mini Project: REPL Calculator (within REPL)

# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))
# print("Sum is: ", num1 + num2)
# print("Difference is: ", num1 - num2)
# print("Product is: ", num1 * num2)
# print("Quotient is: ", num1 / num2)

# //? Explanation

# input() = Read
# int() = Eval
# print() = Print
# Loop = Ready for next

# //! ASCII code 

# print(ord('A'))
# print(ord('a'))
# print(chr(65))
# print(chr(97))
# print(ord('₹'))
# print(chr(8364))
# print(ord("😭"))

# //! Lucky Number Fortune

# name = input("Enter your name: ")
# day = input("Enter day of the week(in numbers): ")

# lucky_number = ord(name[0]) + ord(name[-1]) + int(day)

# print(lucky_number)

# //! Walrus Operator (:=) in REPL only
# assigns + print in one line
# e.g, print(name := "Ashu")


# //! Color text output in terminal (without external libraries)
# # Red text
# print("\033[91mThis is red text\033[0m")

# # Green text
# print("\033[92mThis is green text\033[0m")

# # Yellow text
# print("\033[93mThis is yellow text\033[0m")

# # Blue text
# print("\033[94mThis is blue text\033[0m")

# # Bold text
# print("\033[1mThis is bold text\033[0m")

# # Italic text
# print("\033[3mThis is italic text\033[0m")

# # Underline text
# print("\033[4mThis is underlined text\033[0m")

# # Strikethrough text
# print("\033[9mThis is struck through text\033[0m")

# # With variables
# name = "ashu"
# print("\033[94mHello " + name + "\033[0m")

# Mini math with pow(), round(), divmod()
# print(pow(2, 3))

# print(round(3.4145672389, 2))

# print(divmod(10, 3)) # gives the quotient and the remainder

# //! Opens a cartoon in browser

# import antigravity


# //! Using built-in datetime module

# from datetime import date
# birth_year = 2004
# age = date.today().year - birth_year
# print(age)

# //! Age calculator using custom current year format

# birth_year = 2004
# current_year = 2026

# age = current_year - birth_year
# print(age)


# //! PROJECT
# ?Drem Job Predictor

name = input("Enter your name: ")
month = input("Enter your birth month: ")

print("/n Your dream job is: ")

if month.lower() == "january":
    print("AI Engineer")

elif month.lower() == "february":
    print("Data Scientist")

elif month.lower() == "march":
    print("Web Developer")

elif month.lower() == "april":
    print("Machine Learning Engineer")

elif month.lower() == "may":
    print("Software Engineer")

elif month.lower() == "june":
    print("Cloud Engineer")

elif month.lower() == "july":
    print("DevOps Engineer")

elif month.lower() == "august":
    print("Network Engineer")

elif month.lower() == "september":
    print("Cyber Security Engineer")

elif month.lower() == "october":
    print("DevOps Engineer")

elif month.lower() == "november":
    print("Cloud Engineer")

elif month.lower() == "december":
    print("Game Developer")

else :
    print("Invalid Input")
    
