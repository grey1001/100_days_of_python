import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

name = input("Enter your name :")
print(f"Welcome {name} and good luck!")

random_word = random.choice(words)
print("Guess the characters")
guesses = ""

turns = 5

while turns > 0:
    failed = 0
    
    for char in random_word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
    if failed == 0:
        print("You win")
        print(f"The word is {random_word}")
        break
    print()
    guess = input("guess a character: ")
    guesses += guess

    if guess not in random_word:
        turns -= 1
        print("Wrong")

        print(f"You have {+ turns} more guesses")

        if turns == 0:
            print("You lose")