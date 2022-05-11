from turtle import Turtle

ALIGNMENT = "center"
FONT = ("맑은 고딕", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)

        self.update_point()

    def update_point(self):
        self.write(f"점수: {self.score}", False, align=ALIGNMENT, font=FONT)

    def plus_point(self):
        self.score += 1
        self.clear()
        self.update_point()

    def game_over(self):
        self.home()
        self.write("게임 오버", False, align=ALIGNMENT, font=FONT)
