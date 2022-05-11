from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

board = Scoreboard()

game_is_on = True
while game_is_on:
    """
    update는 옛날 티비가 한줄씩 추가되어 나오던 것을 생각하면 편하다
    update로 동작을 한꺼번에 보여줄 수 있다
    """
    screen.update()
    time.sleep(0.1)
    snake.move()

    # 뱀이 먹이를 먹었을 때
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        board.plus_point()

    # 뱀이 벽과 부딪쳤을 때
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        board.game_over()

    # 뱀의 머리와 꼬리가 부딪쳤을 때
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            board.game_over()

screen.exitonclick()
