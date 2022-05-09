from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    """
    update는 옛날 티비가 한줄씩 추가되어 나오던 것을 생각하면 편하다
    update로 동작을 한꺼번에 보여줄 수 있다
    """
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
