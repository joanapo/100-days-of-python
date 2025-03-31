import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tommy = Turtle()
tommy.width(15)
tommy.speed("fastest")

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colour = (r, g, b)
    return random_colour

directions = [0, 90, 180, 270]

for _ in range(200):
    tommy.color(random_colour())
    tommy.fd(30)
    tommy.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()