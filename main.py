from turtle import Turtle, Screen, colormode
import random

colormode(255)
sam = Turtle()
sam.shape("classic")
sam.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color


sam.hideturtle()


sam.penup()
sam.goto(-260,-230)
sam.pendown()

going = True


for x in range(5):

    for _ in range(11):
        sam.dot(20, (random_color()))
        sam.penup()
        sam.forward(50)

    sam.left(90)
    sam.forward(50)
    sam.left(90)
    sam.forward(50)

    for _ in range(11):
        sam.dot(20, (random_color()))
        sam.penup()
        sam.forward(50)

    sam.right(90)
    sam.forward(50)
    sam.right(90)
    sam.forward(50)


screen = Screen()
screen.exitonclick()
