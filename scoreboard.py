from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.point_a = 0
        self.point_b = 0
        self.hideturtle()
        self.penup()

        self.update_points()

    def update_points(self):
        self.goto(0, 260)
        self.write(f"Score", move=False, align="center", font=("arial", 18, "normal"))
        self.goto(0, 210)
        self.write(f"{self.point_a} | {self.point_b}", move=False, align="center", font=("arial", 26, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=("arial", 20, "normal"))

    def track_point_a(self):
        self.point_a += 1
        self.clear()
        self.update_points()

    def track_point_b(self):
        self.point_b += 1
        self.clear()
        self.update_points()