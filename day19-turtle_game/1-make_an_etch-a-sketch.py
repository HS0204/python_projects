from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def counter_clockwise():
    turtle.left(10)
    ### 강의 코드
    """
    new_heading = turtle.heading() + 10
    turtle.seth(new_heading)
    """


def clockwise():
    turtle.right(10)


def clear():
    turtle.reset()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()
