from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.b = None
        self.create_ball()
        self.x = 10
        self.y = 10
        self.ball_speed = 0.1

    def create_ball(self):
        self.penup()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")

    def move_ball(self):
        x_pos = self.xcor() + self.x
        y_pos = self.ycor() + self.y
        self.goto(x_pos, y_pos)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.ball_speed *= 0.9

    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()
        self.ball_speed = 0.1

