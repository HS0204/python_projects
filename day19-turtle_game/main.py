from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


def make_turtle():
    for idx in range(len(colors)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[idx])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=(-75 + (idx * 30)))
        all_turtles.append(new_turtle)


def race(bet, is_race_on):
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == bet:
                    print(f"이겼습니다! {winning_color} 거북이 가장 먼저 도착했습니다!")
                else:
                    print(f"졌습니다! {winning_color} 거북이 가장 먼저 도착했습니다!")

            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=500, height=400)
    make_turtle()

    user_bet = screen.textinput(title="내기", prompt="어떤 색깔의 거북이가 우승할지 \"영어로\" 입력해주세요")

    race(user_bet, True)

    screen.exitonclick()
