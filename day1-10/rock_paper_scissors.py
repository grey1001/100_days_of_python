import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random() # to expand the range of the values printed by the random float fn simply multiply by an integer. E.G * 5 because this only prints between 0 and 0.9999
# print(random_float)


toss = random.randint(0, 1)

if toss == 1:
    print("Heads")
else:
    print("Tails")