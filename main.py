from turtle import Screen
from shooter import Shooter
from beem import Beem
from aliens import AlienManager
from shield import Shield
from scoreboard import Scoreboard
import random


screen = Screen()
screen.bgcolor("black")
screen.setup(width=1100, height=900)
screen.title("Space Invaders")
screen.tracer(0)

shooter = Shooter((0, -350))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(shooter.go_right, "Right")
screen.onkey(shooter.go_left, "Left")

alien_manager = AlienManager()
alien_manager.create_block()

shields = Shield()
shields.create_shields()

beem_list = {}
alien_beem_list = {}
shoot_level = 70
lives = 5
big_alien_true = True


def shoot_beem():
    beem = Beem()
    beem.goto(shooter.xcor(), -320)
    beem_list[beem] = shooter.xcor()

def alien_shoot_beem():
    beem = Beem()
    random_alien = random.choice(alien_manager.all_aliens)
    beem.goto(random_alien.xcor(), random_alien.ycor())
    alien_beem_list[beem] = random_alien.xcor()

game_is_on = True
while game_is_on:
    screen.update()

    for b in beem_list:
        b.shoot(beem_list[b])
    for a in alien_beem_list:
        a.alien_shoot(alien_beem_list[a])

    screen.onkey(shoot_beem, "space")

    if random.randint(1, shoot_level) == 1:
        alien_shoot_beem()

    alien_manager.move()

    # Detect collision with block
    for alien in alien_manager.all_aliens:
        hit = False
        holder = None
        for b in beem_list:
            if alien.distance(b) < 45:
                alien_manager.hit_alien(alien)
                hit = True
                holder = b
        if hit:
            holder.hideturtle()
            del beem_list[holder]
            shoot_level -= 1
            scoreboard.point()

    shooter_hit = False
    shooter_holder = None
    for b in alien_beem_list:
        if shooter.distance(b) < 45:
            lives -= 1
            shooter_hit = True
            shooter_holder = b
            scoreboard.update_lives(lives)
            print(lives)
            if lives == 0:
                print("game over")
                scoreboard.game_over()
                game_is_on = False
            else:
                shooter.hit_shooter()
    if shooter_hit:
        shooter_holder.hideturtle()
        del alien_beem_list[shooter_holder]

    if alien_manager.all_aliens == []:
        alien_manager.x = -50
        alien_manager.y = 50
        shoot_level = 70
        lives += 2
        for a in alien_beem_list:
            a.hideturtle()
        for b in beem_list:
            b.hideturtle()
        beem_list.clear()
        alien_beem_list.clear()
        alien_manager.create_block()
        scoreboard.level_up()
        scoreboard.update_lives(lives)

    for shield in shields.all_shields:
        hit = False
        holder = None
        for b in beem_list:
            if shield.distance(b) < 45:
                hit = True
                holder = b, 'b'
        for a in alien_beem_list:
            if shield.distance(a) < 45:
                hit = True
                holder = a, 'a'
        if hit:
            shields.hit_shield(shield)
            if holder[1] == 'b':
                holder[0].hideturtle()
                del beem_list[holder[0]]
                hit = False
            if holder[1] == 'a':
                holder[0].hideturtle()
                del alien_beem_list[holder[0]]
                hit = False
    if shields.remove:
        # print(shields.all_shields, shields.holder)
        shields.remove_shield()

    if scoreboard.score % 40 == 0 and big_alien_true and scoreboard.score != 0:
        alien_manager.big_alien()
        big_alien_true = False
    alien_manager.big_move()
    if scoreboard.score % 66 == 0:
        big_alien_true = True

    big_hit = False
    big_holder = None
    for b in beem_list:
        if alien_manager.big.distance(b) < 45:
            alien_manager.big_hit()
            big_hit = True
            big_holder = b

    if big_hit:
        big_holder.hideturtle()
        del beem_list[big_holder]
        scoreboard.score += 25
        scoreboard.update_scoreboard()


screen.exitonclick()