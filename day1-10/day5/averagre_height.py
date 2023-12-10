# fruits = ["apples", "peach", "pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "pie")

# for loop with range
total = 0
for number in range(1, 101):
    total += number
print(total)


# heights = [int(height) for height in input("Enter the heights of your students separated by commas: ").split(",")]
# counter = 0
# total = 0
# for n in heights:
#     # total += n
#     total = total + n # this is another way to do it
# print("total height = ", total)

# for n in heights:
#     counter += 1 # this helps to accumulate the number of students by using +=
# print(f"number of students = {counter}")

# average = round(total / counter)
# print(f"average height = {average}")