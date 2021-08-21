from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.coordinates = coordinates
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(self.coordinates[0], 0)
        self.shapesize(5, 1)

    def move_up(self):
        y_coord = self.ycor() + 20
        self.goto(self.xcor(), y_coord)

    def move_down(self):
        y_coord = self.ycor() - 20
        self.goto(self.xcor(), y_coord)
