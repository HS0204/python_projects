from turtle import Turtle, Screen, colormode
import random

turtle = Turtle()
turtle.shape("turtle")
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

angles = [0, 90, 180, 270]
turtle.pensize(13)
turtle.speed(10)

def random_walk():
    turtle.color(random_color())
    turtle.forward(30)
    turtle.seth(random.choice(angles))

while True:
    random_walk()

screen = Screen()
screen.exitonclick()
