from turtle import Screen,Turtle
from padle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
s.title("pong game")
s.setup(width=800, height=600)
s.bgcolor("black")
s.tracer(0)

p = Paddle()
b = Ball()
score = Scoreboard()

s.listen()
s.onkey(p.a_up, "w")
s.onkey(p.a_down, "s")
s.onkey(p.b_up, "Up")
s.onkey(p.b_down, "Down")

is_game_on = True
while is_game_on:
    s.update()
    time.sleep(b.ball_speed)
    b.move_ball()
    # collision with top and bottom wall
    if b.ycor() < -280 or b.ycor() > 280:
        b.bounce_y()
    # collision with right paddle
    if b.distance(p.paddle[1]) < 50 and b.xcor() > 360:
        b.bounce_x()
    # right paddle misses ball
    elif b.distance(p.paddle[1]) > 50 and b.xcor() == 400:
        b.reset_ball()
        score.track_point_a()

    # collision with left paddle
    if b.distance(p.paddle[0]) < 50 and b.xcor() < -360:
        b.bounce_x()
    # left paddle misses ball
    elif b.distance(p.paddle[0]) > 50 and b.xcor() == -400:
        b.reset_ball()
        score.track_point_b()
    if score.point_a >= 10 or score.point_b >= 10:
        score.game_over()
        is_game_on = False
s.exitonclick()
