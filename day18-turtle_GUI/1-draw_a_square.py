from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("forest green")

for _ in range(4):
    turtle.forward(100)
    turtle.right(90)


screen = Screen()
screen.exitonclick()