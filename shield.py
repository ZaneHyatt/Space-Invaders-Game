from turtle import Turtle


class Shield(Turtle):

    def __init__(self):
        self.all_shields = {}
        self.x = -400
        self.shield_level = 0
        self.remove = False
        self.holder = None

    def create_shields(self):
        for i in range(5):
            new_shield = Turtle("square")
            new_shield.shapesize(stretch_wid=2, stretch_len=5)
            new_shield.penup()
            new_shield.goto(self.x, -175)
            new_shield.color('light green')
            self.x += 200
            self.all_shields[new_shield] = self.shield_level

    def hit_shield(self, shield):
        self.all_shields[shield] = ((self.all_shields.get(shield)) + 1)
        if self.all_shields.get(shield) >= 10:
            shield.color('green')
        if self.all_shields.get(shield) >= 20:
            shield.color('#004000')
        if self.all_shields.get(shield) >= 25:
            shield.color('#002600')
        if self.all_shields.get(shield) >= 35:
            self.remove = True
            self.holder = shield

    def remove_shield(self):
        self.holder.hideturtle()
        del self.all_shields[self.holder]
        self.remove = False

