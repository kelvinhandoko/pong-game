from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG-GAME")
screen.tracer(0)

l_paddle = Paddle((-360, 0))
r_paddle = Paddle((360, 0))

ball = Ball()

score_board = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)


game_start = True
while game_start:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.wall_detect()
    ball.paddle_detect(l_paddle=l_paddle, r_paddle=r_paddle)
    if ball.xcor() > 400:
        ball.reset_position()
        score_board.add_l_score()

    if ball.xcor() < -400:
        ball.reset_position()
        score_board.add_r_score()
screen.exitonclick()
