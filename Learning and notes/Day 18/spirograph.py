import turtle as t
import random

tammy = t.Turtle()
t.colormode(255)
tammy.speed("fastest")

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour = (r, g, b)
    return colour

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tammy.color(random_colour())
        tammy.circle(100)
        tammy.setheading(tammy.heading() + size_of_gap)

draw_spirograph(3)

screen = t.Screen()
screen.exitonclick()