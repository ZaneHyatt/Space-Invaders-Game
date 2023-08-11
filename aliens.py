from turtle import Turtle


class AlienManager(Turtle):

    def __init__(self):
        self.all_aliens = []
        self.x = -50
        self.y = 50
        self.x_move = 0.5
        self.left = True
        self.big = Turtle("circle")

    def create_block(self):
        # x = -50
        # y = 50
        for i in range(60):
            new_alien = Turtle("turtle")
            new_alien.tilt(-90)
            new_alien.shapesize(stretch_wid=1.5, stretch_len=1.5)
            new_alien.penup()
            new_alien.goto(self.x, self.y)
            new_alien.color('white')
            self.x += 60
            if (i == 9) or (i == 19) or (i == 29) or (i == 39) or (i == 49):
                self.y += 50
                self.x = self.x - 600
            self.all_aliens.append(new_alien)

    def big_alien(self):
        self.big.shapesize(stretch_wid=1.5, stretch_len=5)
        self.big.penup()
        self.big.goto(650, 345)
        self.big.color('purple')

    def hit_alien(self, alien):
        alien.hideturtle()
        self.all_aliens.remove(alien)

    def move(self):
        for alien in self.all_aliens:
            new_y = (alien.pos())[1]
            if (alien.pos())[0] <= -490:
                self.left = False
            if (alien.pos())[0] >= 490:
                self.left = True
            if self.left:
                new_x = ((alien.pos())[0]) - self.x_move
            else:
                new_x = ((alien.pos())[0]) + self.x_move
            alien.goto(new_x, new_y)

    def big_move(self):
        new_x = self.big.xcor() - 3
        self.big.goto(new_x, 330)

    def big_hit(self):
        self.big.hideturtle()
