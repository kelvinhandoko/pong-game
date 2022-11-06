from turtle import Turtle


class Ball(Turtle):
    def __init__(self, size: int = 1) -> None:
        """
        size untuk memperbesar bola
        """
        super().__init__()
        self.shapesize(stretch_len=size, stretch_wid=size)
        self.color("white")
        self.shape("circle")
        self.penup()
        self.y_move = 20
        self.x_move = 20
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def wall_detect(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

    def paddle_detect(self, l_paddle, r_paddle):
        if self.distance(r_paddle) < 50 and self.xcor() > 325 or self.distance(l_paddle) < 50 and self.xcor() < -325:
            self.bounce_x()

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
