from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.level = 1
        self.live = 5
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-450, 365)
        self.write(f"SCORE: {self.score}", align="center", font=("Press Start 2P", 25, "normal"))
        self.goto(-250, 365)
        self.write(f"LEVEL: {self.level}", align="center", font=("Press Start 2P", 25, "normal"))
        self.goto(350, 365)
        self.write(f"LIVES: {self.live}", align="center", font=("Press Start 2P", 25, "normal"))


    def point(self):
        self.score += 1
        self.update_scoreboard()

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def update_lives(self, lives):
        self.live = lives
        self.update_scoreboard()

    def game_over(self):
        self.update_scoreboard()
        self.goto(0, 0)
        self.color('red')
        self.write("GAME OVER", align="center", font=("Press Start 2P", 60, "normal"))

