# Create a list of names.
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

# # Generate a random index within the range of the list 'names'.
# # random.randint(a, b) returns a random integer N such that a <= N <= b.
random_name = random.randint(0, len(names) - 1) # here we subtract the numbers from the list by 1 to respect the indexing which goes from 0 to -1

# # Use the randomly generated index to access a name from the 'names' list.
random_output = names[random_name]

# Print the randomly selected name.
print(random_output)