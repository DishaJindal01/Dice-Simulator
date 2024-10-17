import random

while True:
    print("Choose a colour for your dice: \nR for red\nB for blue\nG for green\nQ to quit")
    user = input("Enter: ")
    user = user.casefold()
    
    if user == "r":
        rd = random.choices([1, 2, 3, 4, 5, 6], weights=[1, 1, 1, 1, 1, 5])[0]
        print("Red Dice:", rd)
    elif user == "b":
        bl = random.choices([1, 2, 3, 4, 5, 6], weights=[3, 1, 1, 1, 1, 1])[0]
        print("Blue Dice:", bl)
    elif user == "g":
        gr = random.choices([1, 2, 3, 4, 5, 6])[0]
        print("Green Dice:", gr)
    elif user == "q":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")
