from game_data import data
import random
from art import logo, vs
from replit import clear


score = 0
current_score = score
choice2 = random.choice(data)
choice1 = random.choice(data)


def random_choice(choice1, choice2):   
    while choice2 == choice1:
        choice2 = random.choice(data)
    return(choice2)

while True:
    print(logo)
    print(f"psst Choice one is {choice1['follower_count']} and choice two is {choice2['follower_count']}")
    print(f"Compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']}")
    print(vs)
    print(f"Compare B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}")
    option = input("Who has more followers? Type 'A' or 'B': ").upper()

    if option == 'A' or option == 'B':
        if choice1['follower_count'] < choice2['follower_count']:
            score += 1
            current_score = score
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
