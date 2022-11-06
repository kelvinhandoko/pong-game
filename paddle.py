from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinate) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(coordinate)

    def go_up(self):
        new_y = self.ycor() + 20
        if self.ycor() > 220:
            new_y = self.ycor()
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if self.ycor() < -220:
            new_y = self.ycor()
        self.goto(self.xcor(), new_y)
