# Define three lines, each representing a row in the 3x3 grid.
line1 = ["⬜️", "⬜️", "⬜️"]
line2 = ["⬜️", "⬜️", "⬜️"]
line3 = ["⬜️", "⬜️", "⬜️"]

# Create a 2D list 'map' that contains the three lines, forming a 3x3 grid.
map = [line1, line2, line3]

# Print a message indicating that the program is hiding a treasure.
print("Hiding your treasure! X marks the spot.")

# Prompt the user to input the position where they want to put the treasure.
position = input()  # For example, the user might enter "A2".

# Extract the first character (letter) from the user's input and convert it to lowercase.
letter = position[0].lower()

# Define a list 'abc' containing the letters "a", "b", and "c".
abc = ["a", "b", "c"]

# Find the index of the letter in the 'abc' list.
letter_index = abc.index(letter)

# Extract the second character (number) from the user's input, convert it to an integer, and subtract 1.
number_index = int(position[1]) - 1

# Update the map by placing the treasure ("X") at the specified position.
map[number_index][letter_index] = "X"

# Print the updated map with the treasure marked.
print(f"{line1}\n{line2}\n{line3}")
