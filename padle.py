from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.a_pos = (-280, 0)
        self.b_pos = (280, 0)
        self.p = None
        self.paddle = []
        self.create_paddle()

    def create_paddle(self):
        for i in range(1, 3):
            self.p = Turtle("square")
            # self.shape("square")
            self.speed("fastest")
            self.p.color("white")
            self.p.shapesize(stretch_len=1, stretch_wid=5)
            self.p.penup()
            if i == 1:
                self.p.goto(-380, 0)
            elif i == 2:
                self.p.goto(375, 0)
            self.paddle.append(self.p)

    def a_up(self):
        print(self.paddle[0].ycor())
        new_y = self.paddle[0].ycor() + 20
        self.paddle[0].goto(self.paddle[0].xcor(), new_y)
        print("move up")
        print(new_y)

    def a_down(self):
        new_y = self.paddle[0].ycor() - 20
        self.paddle[0].goto(self.paddle[0].xcor(), new_y)
        print("move down")

    def b_up(self):
        new_y = self.paddle[1].ycor() + 20
        self.paddle[1].goto(self.paddle[1].xcor(), new_y)

    def b_down(self):
        new_y = self.paddle[1].ycor() - 20
        self.paddle[1].goto(self.paddle[1].xcor(), new_y)
