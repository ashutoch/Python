
#! if , else, elif

# is_raining = True

# if is_raining:
#     print("Sleep")

# else:
#     print("Sote hi raho chutti hai")

#! Ternary Condition
# age = 20

# status = "Adult" if age >= 18 else "Minor"

# print(status)


#! Haunted Treasure Door / Door of Luck

import random

print("Welcome to the door of luck")
print("You're in a room with 3 doors. One will help you escape and others may trap you")

correct_door = random.randint(1,3) # selects a door in btw 1 and 3

choice = int(input("Choose a door (1, 2, 3): "))

if choice == correct_door:
    print("Congrats you choose the correct door...")

elif choice == 1 or choice == 2 or choice == 3:
    print("Sorry Wrong Door...")

else:
    print("Invalid Door")

print("The correct door was: ", correct_door)