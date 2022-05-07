from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")

### 내 코드
for angle in range(3, 11):
    colours = ["forest green", "salmon", "plum", "light sky blue", "navajo white", "tomato", "yellow green",
               "cornflower blue", "dark orchid"]
    choice_colour = random.choice(colours)
    turtle.color(choice_colour)

    for _ in range(angle):
        turtle.forward(100)
        turtle.right(360 / angle)

    colours.remove(choice_colour)

### 강의 코드
"""
colours = ["forest green", "salmon", "plum", "light sky blue", "navajo white", "tomato", "yellow green", "cornflower blue", "dark orchid"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)

for shape_side_n in range(3, 11):
    turtle.color(random.choice(colours))
    draw_shape(shape_side_n)
"""

screen = Screen()
screen.exitonclick()
