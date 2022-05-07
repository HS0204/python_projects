from turtle import Turtle, Screen, colormode
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(0)
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_circle():
    turtle.color(random_color())
    turtle.circle(100)

### 내 코드
"""
for angle in range(0, 360, 5):
    draw_circle()
    turtle.seth(angle)
"""

### 강의 코드
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        draw_circle()
        turtle.setheading(turtle.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()
