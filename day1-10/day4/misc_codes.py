import random
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

options = [rock, paper, scissors]
random_choice = random.randint(0,2)
print("Welcome to the game")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
print("Your choice:")
print(options[user_choice])


print("Computer chose:")
print(options[random_choice])
if random_choice == user_choice:
    print("It's a draw, play again")
elif user_choice == 0 and random_choice == 1:
    print("You lose")
elif user_choice == 0 and random_choice == 2:
    print("You win")
elif user_choice == 1 and random_choice == 0:
    print("You win")
elif user_choice == 1 and random_choice == 2:
    print("You lose")
elif user_choice == 2 and random_choice == 0:
    print("You lose")
elif user_choice == 2 and random_choice == 1:
    print("You win")