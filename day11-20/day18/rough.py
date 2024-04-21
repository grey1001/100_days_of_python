from turtle import *
import random 


tim = Turtle()
tim.shape("triangle")
colors = colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return(r,g,b)

tim.speed('fastest')
def draw_spiro(size_of_gap): 
    for _ in range(int(360/size_of_gap)):       
        tim.circle(200)
        tim.color(random_color())
        tim.setheading(tim.heading()+size_of_gap)

draw_spiro(5)

screen = Screen()
screen.exitonclick()