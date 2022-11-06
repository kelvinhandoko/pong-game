from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align="center", font=("Consolas", 40, "normal"))
        self.goto(0, 245)
        self.write(":", align="center", font=("Consolas", 40, "normal"))
        self.goto(100, 240)
        self.write(self.r_score, align="center", font=("Consolas", 40, "normal"))

    def add_l_score(self):
        self.l_score += 1
        self.update()

    def add_r_score(self):
        self.r_score += 1
        self.update()
