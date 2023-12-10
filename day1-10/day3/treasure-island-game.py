# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆


# bill = 15

#Write your code below this line 👇
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25


# if add_pepperoni == "Y":
#     if size == "S":
#       bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")


# if size == "S" and add_pepperoni == "Y" and extra_cheese == "Y":
#     bill += 3
#     print(f"Your final bill is: ${bill}.")
# elif size == "S" and add_pepperoni == "N" and extra_cheese == "Y":
#     bill += 1
#     print(f"Your final bill is: ${bill}.")
# elif size == "S" and add_pepperoni == "Y" and extra_cheese == "N":
#     bill += 2
#     print(f"Your final bill is: ${bill}.")
# elif size == "S" and add_pepperoni == "N" and extra_cheese == "N":
#     print(f"Your final bill is: ${bill}.")

# print("Welcome to the coaster")
# height = int(input("Enter your height in cm: "))
# bill = 0

# if height >= 120:
#     print("You can ride the coaster")
#     age = int(input("Enter your age:"))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5")
#     elif age <= 18:
#         bill = 10
#         print("Youth tickets are $10")
#     else:
#         bill = 15
#         print("Youth tickets are $15")
#     photo_taken = input("Do you want your foto taken?, Select Y or N ")
#     bill += 3
#     if photo_taken == "Y":
#         print(f"Your bill is {bill}")
# else:
#     print("Sorry you can't ride the coaster yet.")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************

''')

print("Welcome to the treasure Island.\nYour mission is to find the treasure.")
first_choice = input("You are at a crossroad. Where would you like to go?, Choose left or right:\n")


if first_choice == "right":
    print("Fell into a hole.\nGame over")
elif first_choice == "left":
    second_choice = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across?\n")
    if second_choice == "swim":
        print("Attacked by trout.\nGame over")
    elif second_choice == "wait":
        third_choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if third_choice == "red":
            print("You have been burned by fire.\nGame over")
        elif third_choice == "blue":
            print("You have been eaten by beasts.\nGame over")
        elif third_choice == "yellow":
            print("You win!,\nCongratulations!!")
        else:
            print("Game over")

