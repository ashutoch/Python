
#! List: collection of items that is ordered, changable and allows duplicate

# fruits = ['apple', 'banana', 'kiwi']
# print(fruits)

# fruits[1] = 'strawberry'
# print(fruits)

#? adding elements to a list

# fruits.append('grapes')     # inserts at the last
# print(fruits)

# fruits.insert(2, 'banana')      # inserts at a specific position
# print(fruits)

#? removing items from the list

# fruits.remove('apple')      # removes a particular thing from list
# print(fruits)

# fruits.pop()
# print(fruits)       # removes the last element

# del fruits[1]       # removes items using index 
# print(fruits)


#! Length and looping
# fruits = ['apple', 'banana', 'kiwi', 'grapes']

# print(len(fruits))

# for item in fruits:
#     print(item)


#! List slicing
# fruits = ['apple', 'banana', 'kiwi', 'grapes']

# print(fruits[ 0 : 2 ])
# print(fruits[ : 2 ])
# print(fruits[ 0 : ])
# print(fruits[ : : -1 ])



#! List Comprehension

# num = [ 10, 20, 30, 40, 50 ]
# square = [ x*x for x in num ]

# square = [ x*x for x in range(10) ]     # gives the square of all numbers from 0 to 9
# print(square)


#! Nested lists

# matrix = [ [1, 2], [3, 4], [5, 6] ]
# print(matrix)
# print(matrix[0] [1])


#! Sorting and Reversing

# num = [2, 5, 1, 6, 9, 10, 3, 0, 4, 8, 7]

# num.sort()
# print(num)

# num.reverse()
# print(num)






#! Turn your python project into a web app (without JS)
#? What is Streamlit?
#? It is an open-source python library that lets you create web apps for Data Science, Machine Learning, AI and Automation without needing HTML, CSS, or JS


import streamlit as st

st.title("Welcome to My New Learning Path")
st.header("AI ML Demo For Self-Learning")

if st.button("Press me!"):
    st.success("Yay you can read🥹")

name = st.text_input("Your name: ")
if name:
    st.write(f"Hello, {name}! \nWelcome to the trial website.")

age = st.slider("Select your age...", 0, 100)
if age < 18:
    st.write("Man you are a kid!!!")

elif age > 18 and age < 30:
    st.write("Young Man")

elif age > 30 and age < 60:
    st.write("Old Dude")

else:
    st.write("How are you still alive!")