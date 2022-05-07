import colorgram
from turtle import Turtle, Screen, colormode
import random


def color_picker():
    colors_in_img = colorgram.extract('image.jpg', 30)
    my_color = []

    for idx in range(len(colors_in_img)):
        color = colors_in_img[idx]
        rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
        my_color.append(rgb)

    return my_color


def remove_color(lst):
    colors = []
    for idx in range(len(lst)):
        r = lst[idx][0]
        g = lst[idx][1]
        b = lst[idx][2]
        if r <= 230 and g <= 230 and b <= 230:
            colors.append((r, g, b))

    return colors


def draw_dot(lst):
    turtle.color(random.choice(lst))
    turtle.dot(20)


def draw_spot_painting(color_lst, row, col):
    # 시작 위치 선정
    turtle.seth(225)
    turtle.forward(300)
    (x, y) = turtle.pos()
    turtle.seth(0)

    for i in range(1, row+1):
        for _ in range(col):
            draw_dot(color_lst)
            turtle.forward(50)
        turtle.penup()
        turtle.goto(x, y + 50 * i)


if __name__ == '__main__':
    colormode(255)

    turtle = Turtle()
    turtle.speed(0)
    turtle.penup()
    turtle.hideturtle()

    color_list = remove_color(color_picker())
    draw_spot_painting(color_list, 10, 10)

    screen = Screen()
    screen.exitonclick()
