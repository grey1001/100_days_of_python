from game_data import data
import random
from art import logo, vs
from replit import clear

current_score = 0
choice2 = random.choice(data)
choice1 = random.choice(data)
def random_choice(choice1, choice2):   
    while choice2 == choice1:
        choice2 = random.choice(data)
    return(choice2)

while True:
    print(logo)
    print(f"Compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']}")
    print(vs)
    print(f"Against B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}")
    option = input("Who has more followers? Type 'A' or 'B': ").upper()
    clear()
    print(logo)
    if option == 'A':
        
        if choice1['follower_count'] > choice2['follower_count']:
            current_score += 1
            previous_choice2 = choice2
            choice1 = previous_choice2
            choice2 = random_choice(choice1,choice2)
            
            print(f"You are right! Current score: {current_score}. ")
    elif option =='B':
        if choice1['follower_count'] < choice2['follower_count']:
            current_score += 1
            previous_choice2 = choice2
            choice1 = previous_choice2
            choice2 = random_choice(choice1,choice2)
            print(f"You are right! Current score: {current_score}. ")

            continue
        else:
            print(f"Sorry that's wrong. Final score {current_score}")
            ask = input("Do you want to try again? 'Y' or 'N' ").upper()
            if ask == 'Y':
                clear() 
                print(logo)
                choice2 = random.choice(data)
                choice1 = random.choice(data)
                choice2 = random_choice(choice1,choice2)
                continue
            else:
                break
    else:
        print("Choose a valid option")
