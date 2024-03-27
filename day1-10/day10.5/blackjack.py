import random
from art import logo
print(logo)

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    def scenario(user_final, computer_final, user_cards, computer_cards):
            
        if computer_final == user_final and computer_final < 21 and user_final < 21:
            print(f"Your final hand: {user_cards}, final score: {user_final} ")
            print(f"Computer's final hand: {computer_cards}, final score {computer_final} ")
            print("It's a draw")
        elif user_final > computer_final and user_final < 21:
            print(f"Your final hand: {user_cards}, final score: {user_final} ")
            print(f"Computer's final hand: {computer_cards}, final score {computer_final} ")
            print("Congrats! you win!")
        elif user_final > 21 and computer_final > 21:
            print(f"Your final hand: {user_cards}, final score: {user_final} ")
            print(f"Computer's final hand: {computer_cards}, final score {computer_final} ")
            print("The game is a bust! You lose")
        elif computer_final > user_final and computer_final < 21:
            print(f"Your final hand: {user_cards}, final score: {user_final} ")
            print(f"Computer's final hand: {computer_cards}, final score {computer_final} ")
            print("You lose!")
        elif user_final < 21 and computer_final > 21:
            print(f"Your final hand: {user_cards}, final score: {user_final} ")
            print(f"Computer's final hand: {computer_cards}, final score {computer_final} ")
            print("Congrats! you win!")
        elif user_final > 21 and computer_final < 21:
            print(f"Your final hand: {user_cards}, final score: {user_final} ")
            print(f"Computer's final hand: {computer_cards}, final score {computer_final} ")
            print("You went over, you lose!")
        elif user_final > 21 and computer_final == 21:
            print(f"Your final hand: {user_cards}, final score: {user_final} ")
            print(f"Computer's final hand: {computer_cards}, final score {computer_final} ")
            print("You went over, you lose!")
        elif user_final == 21 and computer_final < 21:
            print(f"Your final hand: {user_cards}, final score: {user_final} ")
            print(f"Computer's final hand: {computer_cards}, final score {computer_final} ")
            print("You win") 
    question1 = input("Do you want to play a game of blackjack?, type 'y' or 'n' ")
    if question1 == 'y':
        user_cards = random.sample(cards, 2)
        computer_cards = random.sample(cards, 2)
        user_final = sum(user_cards)
        computer_final = sum(computer_cards)
        print(f"Your cards: {user_cards}, current score {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        question2 = input("Type 'y' to get another card, type 'n' to pass: ")
        if question2 == 'y':
            user_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))
            scenario(user_final, computer_final, user_cards, computer_cards)
        
        if computer_final < 17:
            while computer_final < 17:
                computer_cards.append(random.choice(cards))
                computer_final = sum(computer_cards)
                if computer_final >= 21:
                    scenario(user_final, computer_final, user_cards, computer_cards)
                    break
        else:
            scenario(user_final, computer_final, user_cards, computer_cards)
                
    else:
        print("Thank you for playing")


while True:
    deal_cards()
    