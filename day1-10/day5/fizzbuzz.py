game = range(1, 100+1)

for number in game:
    if number % 5 == 0 and number % 3 == 0:
        number = ("FizzBuzz")
    elif number % 3 == 0:
        number = ("Fizz")
    elif number % 5 == 0:
        number = ("Buzz")
    print(number)