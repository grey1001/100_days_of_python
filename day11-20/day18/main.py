from turtle import *
import random 

colormode(255)
color_list = [(248, 247, 240), (239, 250, 245), (251, 240, 247), (236, 243, 250), (236, 226, 85), (211, 159, 109), (115, 176, 211), (202, 5, 69), (231, 53, 126), (195, 77, 20), (215, 133, 176), (194, 163, 14), (33, 106, 169), (10, 20, 65), (30, 189, 116), (232, 224, 4), (18, 28, 172), (234, 165, 197), (121, 187, 159), (203, 31, 130)]

tim = Turtle()
tim.speed("fastest")  # Increase the speed of the turtle
tim.penup()  # Prevents the turtle from drawing lines
tim.ht()

start_x = -200  # Starting x position
start_y = 200  # Starting y position
spacing = 50  # Space between dots

# Draw a 10x10 grid of dots
for row in range(10):
    for column in range(10):
        tim.goto(start_x + column * spacing, start_y - row * spacing)
        dot_color = random.choice(color_list)
        tim.dot(15, dot_color)

screen = Screen()
screen.exitonclick()