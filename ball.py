from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_coord = 10
        self.y_coord = 10
        self.ball_speed = 0.1

    def move_ball(self):
        x_pos = self.xcor() + self.x_coord
        y_pos = self.ycor() + self.y_coord
        self.goto(x_pos, y_pos)

    def bounce_up_down(self):
        self.y_coord *= -1

    def bounce_left_right(self):
        self.x_coord *= -1
        self.ball_speed *= 0.9

    def reset_pos(self):
        self.home()
        self.ball_speed = 0.1
        self.x_coord *= -1
