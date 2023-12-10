 
print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()# this ensures the entire input is in lowercase
t = lower_names.count("t")# the count function here counts the number of times t occurs in the declaredf variable lower_names
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e # this adds everything together

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you got together like coke and mentos")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")