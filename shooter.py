from turtle import Turtle


class Shooter(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("arrow")
        self.color("light green")
        self.tilt(90)
        self.shapesize(stretch_wid=5, stretch_len=2)
        self.penup()
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())

    def hit_shooter(self):
        print("shooter hit")