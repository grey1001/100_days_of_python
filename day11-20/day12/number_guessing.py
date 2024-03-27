import random
from art import logo
computer_choice = random.randint(1, 100)
attempts_hard = 5
attempts_easy = 10
def hard():
    while True:
        global attempts_hard
        guess = int(input("Make a guess: "))
        if guess < computer_choice:
            attempts_hard -= 1
            new_attempt = attempts_hard
            print("Too low.\nGuess again.")
            print(f"You have {new_attempt} attempts remaining to guess the number")
        if guess == computer_choice:
            print(f"Your guess is {guess}, I also guessed {computer_choice}.\nCongratulations, You win:) ")
        if guess > computer_choice:
            attempts_hard -= 1
            new_attempt = attempts_hard
            print("Too high.\nGuess again.")
            print(f"You have {new_attempt} attempts remaining to guess the number")
        if attempts_hard == 0:
            break
        
def easy():
    while True:
        guess = int(input("Make a guess: "))
        global attempts_easy
        if guess < computer_choice:
            attempts_easy -= 1
            new_attempt = attempts_easy
            print("Too low.\nGuess again.")
            print(f"You have {new_attempt} attempts remaining to guess the number")
        if guess == computer_choice:
            print(f"Your guess is {guess}, I also guessed {computer_choice}.\nCongratulations, You win:) ")
        if guess > computer_choice:
            attempts_easy -= 1
            new_attempt = attempts_easy
            print("Too high.\nGuess again.")
            print(f"You have {new_attempt} attempts remaining to guess the number")
        if attempts_easy == 0:
            break
       

print(logo)
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy'or 'hard': ").lower()

if difficulty_level == 'hard':
    print(f"You have 5 attempts remaining to guess the number")
    hard()
    print(f"You've run out of guesses\nMy guess was {computer_choice}, sorry :(")
    
if difficulty_level == 'easy':
    print(f"You have 10 attempts remaining to guess the number")
    easy()
    print(f"You've run out of guesses\nMy guess was {computer_choice}, sorry :(")