from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scores()

    def update_scores(self):
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Comic Sans", 70, "normal"))
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Comic Sans", 70, "normal"))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scores()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scores()

    def game_over(self, player_who_won):
        self.clear()
        if player_who_won == "left":
            self.goto(-130, 190)
            self.write("Left Wins", align="center", font=("Comic Sans", 30, "normal"))
        if player_who_won == "right":
            self.goto(-130, 190)
            self.write("Right Wins", align="center", font=("Comic Sans", 30, "normal"))

        self.goto(150, 190)
        self.write("Game Over.", align="center", font=("Comic Sans", 30, "normal"))
