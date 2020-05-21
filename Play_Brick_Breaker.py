# jackson J.
# 5.21.2020
# Taking what I learned yesterday with Play_Pong, I will try to make brick breaker.
# This will be a lot harder because i will have to find the right window size, and I will have to create a lot of
# Turtle objects that will be destroyed when the ball hits it#
from turtle import *
from random import randint

# Creating The Window
window = Screen()
window.title("Brick_Breaker")
window.bgcolor("black")
window.setup(width=480, height=650)
window.tracer(0)

# Creating The Player
player = Turtle()
player.color("white")
player.shape("square")
player.shapesize(stretch_wid=.5, stretch_len=3)
player.penup()
player.goto(0, 315)


def player_left():
    if player.xcor() > -210:
        x = player.xcor()
        x -= 20
        player.setx(x)


def player_right():
    if player.xcor() < 200:
        x = player.xcor()
        x += 20
        player.setx(x)


# Creating The Player Movement
window.listen()
window.onkeypress(player_left, "a")
window.onkeypress(player_right, "d")
window.onkeypress(player_left, "Left")
window.onkeypress(player_right, "Right")

# Creating the Ball
ball = Turtle()
ball.color("white")
ball.shape("circle")
ball.shapesize(stretch_wid=.5, stretch_len=.5)
ball.penup()
ball.goto(0, 50)
# Giving the ball a random x direction
rand = randint(1, 2)
if rand == 1:
    ball.dx = .2
else:
    ball.dx = -.2
ball.dy = -.2

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() < -230:
        ball.setx(-230)
        ball.dx *= -1

    if ball.xcor() > 230:
        ball.setx(230)
        ball.dx *= -1

    if ball.ycor() < -315:
        ball.sety(-315)
        ball.dy *= -1

    if player.ycor() - 5 < ball.ycor() < player.ycor() and player.xcor() - 30 < ball.xcor() < player.xcor() + 30:
        ball.sety(305)
        ball.dy *= -1

    if ball.ycor() > player.ycor():
        ball.goto(0, 50)
        rand = randint(1, 2)
        if rand == 1:
            ball.dx = .2
        else:
            ball.dx = -.2
        ball.dy *= -1
