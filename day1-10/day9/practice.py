stop = False
people = {}
while stop == False:
    name = input("What is your name?: ")
    age = int(input("What is your age?: "))
    check_question = input("Is there any other player? (yes/no): ")
    people[name] = age
    if check_question != "yes" and check_question != "no":
        print("Please provide a valid response")
    if check_question == "no":
        break
    if check_question == "yes":
        stop == False

highest_age = 0
eldest_person = ""
for person in people:
    oldest_person_age = people[person]
    if oldest_person_age > highest_age:
        highest_age = oldest_person_age
        eldest_person = person
print(f"{name} is {age} years old and thus the eldest")

