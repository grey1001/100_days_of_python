import random

# # random_integer = random.randint(1, 10)
# # print(random_integer)

# # random_float = random.random() # to expand the range of the values printed by the random float fn simply multiply by an integer. E.G * 5 because this only prints between 0 and 0.9999
# # print(random_float)


# toss = random.randint(0, 1)

# if toss == 1:
#     print("Heads")
# else:
#     print("Tails")

# states_of_america = ["New York", "Delaware", "Pennsylvania"]
# states_of_america[0] = "Paris" # this changes the value of item in the list using the index
# states_of_america.append("Tokyo") # This adds something to the list at the end
# print(states_of_america)





rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

game_images = [rock, paper, scissors]
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid choice, you lose")
else:
    print(game_images[user_choice])


    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw, try again")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 1 and computer_choice == 0:
        print("You win")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif user_choice == 2 and computer_choice == 1:
        print("You win")
