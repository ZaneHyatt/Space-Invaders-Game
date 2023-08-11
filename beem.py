from turtle import Turtle


class Beem(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=0.5)
        self.penup()
        self.y_move = 6
        self.move_speed = 0.1

    def shoot(self, x_pos):
        new_x = x_pos
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def alien_shoot(self, x_pos):
        new_x = x_pos
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)


