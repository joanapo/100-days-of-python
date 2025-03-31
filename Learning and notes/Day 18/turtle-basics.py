from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color("pink")

# draw a square
for i in range(4):
    timmy.fd(100)
    timmy.right(90)

# draw a dashed line

for i in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    

# draw a triangle, square, pentagon, hexagon, heptagon...decagon
i = 3
while i < 11:
    for _ in range(i):
        timmy.forward(100)
        timmy.right(360/i)
    i += 1

screen = Screen()
screen.exitonclick()

