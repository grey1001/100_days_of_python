import random

from hangman_art import stages, logo
from hangman_words import word_list
# Get a letter as input from the user


# Choose a random word from the word_list
lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []



print(logo)
for I in range(word_length):
    display += "_"
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])