#  A class is a blueprint from which an object is generated
# The class is normally written with the first letter of each word capitalized
# eg: car = CarBlueprint() this differentiates it from other variables
# So above the car is an object and it gets created from the car blueprint.
# pypi.org  python package index

# from turtle import Turtle, Screen
# timmy = Turtle() # here we imported turtle and tapped into turtle toget Turtle class then assigned it to variable timmy
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.exitonclick())


# class Fruit:
#     def __init__(self, name, clr):#init is where we initialize our attributes. We never have to call it, we oly define it
#         self.name = name
#         self.colour = clr
#     def details(self): #methods are functions related to objects
#         print(f"my {self.name} is {self.colour}")

# apple = Fruit("apple", "red")
# banana = Fruit("banana", "yellow")
# kiwi = Fruit("kiwi", "green")
# apple.details()
# banana.details()


class Guitar:
    def __init__(self):
        self.n_strings = 6
        self.play()
    def play(self):
        print(f"pam pam pam pam pam")

class ElectricGuitar(Guitar): # this is called inheritance. Taking all functionality of parent class and passing to child class
    def __init__(self):
        super().__init__() #to change something in the child class you access the init here. 
        #                   we use the super function to accessthe init of the parent class
        self.n_strings = 8
    def playlouder(self):
        print("pam pam pam pam pam".upper())
my_guitar = ElectricGuitar()
print(my_guitar.n_strings)
print(f"Parent class : {Guitar().n_strings}")


