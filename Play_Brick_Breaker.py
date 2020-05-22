# jackson J.
# 5.21.2020
# Taking what I learned yesterday with Play_Pong, I will try to make brick breaker.
# This will be a lot harder because i will have to find the right window size, and I will have to create a lot of
# Turtle objects that will be destroyed when the ball hits it#
from turtle import *
from random import randint
from time import sleep

# Creating The Window
window = Screen()
window.title("Brick_Breaker")
window.bgcolor("black")
window.setup(width=480, height=650)
window.tracer(0)

# Visual Boundary For the game in full screen
left = Turtle()
left.color("gray")
left.shape("square")
left.shapesize(stretch_wid=32, stretch_len=1)
left.penup()
left.goto(245, 0)

right = Turtle()
right.color("gray")
right.shape("square")
right.shapesize(stretch_wid=32, stretch_len=1)
right.penup()
right.goto(-245, 0)

up = Turtle()
up.color("gray")
up.shape("square")
up.shapesize(stretch_wid=1, stretch_len=25.5)
up.penup()
up.goto(0, 330)

down = Turtle()
down.color("gray")
down.shape("square")
down.shapesize(stretch_wid=1, stretch_len=25.5)
down.penup()
down.goto(0, -277)

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
    if player.xcor() < 210:
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

# Layer 1
a = Turtle()
a.color("red")
a.shape("square")
a.shapesize(stretch_wid=1, stretch_len=4)
a.penup()
a.goto(-194, -90)
a1 = 0

b = Turtle()
b.color("red")
b.shape("square")
b.shapesize(stretch_wid=1, stretch_len=4)
b.penup()
b.goto(-97, -90)
b1 = 0

c = Turtle()
c.color("red")
c.shape("square")
c.shapesize(stretch_wid=1, stretch_len=4)
c.penup()
c.goto(0, -90)
c1 = 0

d = Turtle()
d.color("red")
d.shape("square")
d.shapesize(stretch_wid=1, stretch_len=4)
d.penup()
d.goto(97, -90)
d1 = 0

e = Turtle()
e.color("red")
e.shape("square")
e.shapesize(stretch_wid=1, stretch_len=4)
e.penup()
e.goto(194, -90)
e1 = 0

# Layer 2
f = Turtle()
f.color("red")
f.shape("square")
f.shapesize(stretch_wid=1, stretch_len=4)
f.penup()
f.goto(-144, -127)
f1 = 0

g = Turtle()
g.color("red")
g.shape("square")
g.shapesize(stretch_wid=1, stretch_len=4)
g.penup()
g.goto(-48, -127)
g1 = 0

h = Turtle()
h.color("red")
h.shape("square")
h.shapesize(stretch_wid=1, stretch_len=4)
h.penup()
h.goto(48, -127)
h1 = 0

i = Turtle()
i.color("red")
i.shape("square")
i.shapesize(stretch_wid=1, stretch_len=4)
i.penup()
i.goto(144, -127)
i1 = 0

# Layer 3
j = Turtle()
j.color("red")
j.shape("square")
j.shapesize(stretch_wid=1, stretch_len=4)
j.penup()
j.goto(-194, -164)
j1 = 0

k = Turtle()
k.color("red")
k.shape("square")
k.shapesize(stretch_wid=1, stretch_len=4)
k.penup()
k.goto(-97, -164)
k1 = 0

l_ = Turtle()
l_.color("red")
l_.shape("square")
l_.shapesize(stretch_wid=1, stretch_len=4)
l_.penup()
l_.goto(0, -164)
l_1 = 0

m = Turtle()
m.color("red")
m.shape("square")
m.shapesize(stretch_wid=1, stretch_len=4)
m.penup()
m.goto(97, -164)
m1 = 0

n = Turtle()
n.color("red")
n.shape("square")
n.shapesize(stretch_wid=1, stretch_len=4)
n.penup()
n.goto(194, -164)
n1 = 0

# Layer 4
o = Turtle()
o.color("red")
o.shape("square")
o.shapesize(stretch_wid=1, stretch_len=4)
o.penup()
o.goto(-144, -201)
o1 = 0

p = Turtle()
p.color("red")
p.shape("square")
p.shapesize(stretch_wid=1, stretch_len=4)
p.penup()
p.goto(-48, -201)
p1 = 0

q = Turtle()
q.color("red")
q.shape("square")
q.shapesize(stretch_wid=1, stretch_len=4)
q.penup()
q.goto(48, -201)
q1 = 0

r = Turtle()
r.color("red")
r.shape("square")
r.shapesize(stretch_wid=1, stretch_len=4)
r.penup()
r.goto(144, -201)
r1 = 0

# layer 5
s = Turtle()
s.color("red")
s.shape("square")
s.shapesize(stretch_wid=1, stretch_len=4)
s.penup()
s.goto(-194, -238)
s1 = 0

t = Turtle()
t.color("red")
t.shape("square")
t.shapesize(stretch_wid=1, stretch_len=4)
t.penup()
t.goto(-97, -238)
t1 = 0

u = Turtle()
u.color("red")
u.shape("square")
u.shapesize(stretch_wid=1, stretch_len=4)
u.penup()
u.goto(0, -238)
u1 = 0

v = Turtle()
v.color("red")
v.shape("square")
v.shapesize(stretch_wid=1, stretch_len=4)
v.penup()
v.goto(97, -238)
v1 = 0

w = Turtle()
w.color("red")
w.shape("square")
w.shapesize(stretch_wid=1, stretch_len=4)
w.penup()
w.goto(194, -238)
w1 = 0

# Giving the ball a random x direction
rand = randint(1, 2)
if rand == 1:
    ball.dx = 3
else:
    ball.dx = -3
ball.dy = -3

lives = Turtle()
lives.hideturtle()
lives.speed(0)
lives.goto(0, 100)
lives.penup()
lives.color("gray")
lives.write("Lives Left: 5", align='center', font=("Courier", 20, "bold"))
life = 5

win = 0

totally_not_lazy_mode = True

while life != 0:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if totally_not_lazy_mode:
        player.setx(ball.xcor())

    win = a1 + b1 + c1 + d1 + e1\
        + f1 + g1 + h1 + i1\
        + j1 + k1 + l_1 + m1 + n1\
        + o1 + p1 + q1 + r1\
        + s1 + t1 + u1 + v1 + w1
    if win == 23:
        break

    if ball.xcor() < -230:
        ball.setx(-230)
        ball.dx *= -1

    if ball.xcor() > 230:
        ball.setx(230)
        ball.dx *= -1

    if ball.ycor() < -260:
        ball.sety(-260)
        ball.dy *= -1

    if player.ycor() - 5 < ball.ycor() < player.ycor() and player.xcor() - 30 < ball.xcor() < player.xcor() + 30:
        ball.sety(305)
        ball.dy *= -1

    if ball.ycor() > player.ycor():
        ball.goto(0, 50)
        rand = randint(1, 2)
        if rand == 1:
            ball.dx = 1
        else:
            ball.dx = -1
        ball.dy *= -1
        lives.clear()
        life -= 1
        lives.write(f"Lives Left: {life}", align='center', font=("Courier", 20, "bold"))

    # A check to see if the ball hits a brick
        # Checks the bricks A, J, and S
    if -274 < ball.xcor() < -154:
        if a.ycor() < ball.ycor() < a.ycor() + 15 and a1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            a.hideturtle()
            a1 = 1
        if a.ycor() > ball.ycor() > a.ycor() - 15 and a1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            a.hideturtle()
            a1 = 1

        if j.ycor() < ball.ycor() < j.ycor() + 15 and j1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            j.hideturtle()
            j1 = 1
        if j.ycor() > ball.ycor() > j.ycor() - 15 and j1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            j.hideturtle()
            j1 = 1

        if s.ycor() < ball.ycor() < s.ycor() + 15 and s1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            s.hideturtle()
            s1 = 1
        if s.ycor() > ball.ycor() > s.ycor() - 15 and s1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            s.hideturtle()
            s1 = 1
        # Checks the bricks F and O
    if -184 < ball.xcor() < -104:
        if f.ycor() < ball.ycor() < f.ycor() + 15 and f1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            f.hideturtle()
            f1 = 1
        elif f.ycor() > ball.ycor() > f.ycor() - 15 and f1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            f.hideturtle()
            f1 = 1

        if o.ycor() < ball.ycor() < o.ycor() + 15 and o1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            o.hideturtle()
            o1 = 1
        elif o.ycor() > ball.ycor() > o.ycor() - 15 and o1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            o.hideturtle()
            o1 = 1

        # Checks the bricks B, K, and T
    if -137 < ball.xcor() < -57:
        if b.ycor() < ball.ycor() < b.ycor() + 15 and b1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            b.hideturtle()
            b1 = 1
        elif b.ycor() > ball.ycor() > b.ycor() - 15 and b1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            b.hideturtle()
            b1 = 1

        if k.ycor() < ball.ycor() < k.ycor() + 15 and k1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            k.hideturtle()
            k1 = 1
        elif k.ycor() > ball.ycor() > k.ycor() - 15 and k1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            k.hideturtle()
            k1 = 1

        if t.ycor() < ball.ycor() < t.ycor() + 15 and t1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            t.hideturtle()
            t1 = 1
        elif t.ycor() > ball.ycor() > t.ycor() - 15 and t1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            t.hideturtle()
            t1 = 1

        # Checks the bricks G and P
    if -88 < ball.xcor() < -8:
        if g.ycor() < ball.ycor() < g.ycor() + 15 and g1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            g.hideturtle()
            g1 = 1
        elif g.ycor() > ball.ycor() > g.ycor() - 15 and g1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            g.hideturtle()
            g1 = 1

        if p.ycor() < ball.ycor() < p.ycor() + 15 and p1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            p.hideturtle()
            p1 = 1
        elif p.ycor() > ball.ycor() > p.ycor() - 15 and p1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            p.hideturtle()
            p1 = 1

        # Checks the bricks C, L, and U
    if -40 < ball.xcor() < 40:
        if c.ycor() < ball.ycor() < c.ycor() + 15 and c1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            c.hideturtle()
            c1 = 1
        elif c.ycor() > ball.ycor() > c.ycor() - 15 and c1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            c.hideturtle()
            c1 = 1

        if l_.ycor() < ball.ycor() < l_.ycor() + 15 and l_1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            l_.hideturtle()
            l_1 = 1
        elif l_.ycor() > ball.ycor() > l_.ycor() - 15 and l_1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            l_.hideturtle()
            l_1 = 1

        if u.ycor() < ball.ycor() < u.ycor() + 15 and u1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            u.hideturtle()
            u1 = 1
        elif u.ycor() > ball.ycor() > u.ycor() - 15 and u1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            u.hideturtle()
            u1 = 1

        # Checks the bricks H and Q
    if 88 > ball.xcor() > 8:
        if h.ycor() < ball.ycor() < h.ycor() + 15 and h1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            h.hideturtle()
            h1 = 1
        elif h.ycor() > ball.ycor() > h.ycor() - 15 and h1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            h.hideturtle()
            h1 = 1

        if q.ycor() < ball.ycor() < q.ycor() + 15 and q1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            q.hideturtle()
            q1 = 1
        elif q.ycor() > ball.ycor() > q.ycor() - 15 and q1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            q.hideturtle()
            q1 = 1

        # Check the bricks D, M, and V
    if 137 > ball.xcor() > 57:
        if d.ycor() < ball.ycor() < d.ycor() + 15 and d1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            d.hideturtle()
            d1 = 1
        elif d.ycor() > ball.ycor() > d.ycor() - 15 and d1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            d.hideturtle()
            d1 = 1

        if m.ycor() < ball.ycor() < m.ycor() + 15 and m1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            m.hideturtle()
            m1 = 1
        elif m.ycor() > ball.ycor() > m.ycor() - 15 and m1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            m.hideturtle()
            m1 = 1

        if v.ycor() < ball.ycor() < v.ycor() + 15 and v1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            v.hideturtle()
            v1 = 1
        elif v.ycor() > ball.ycor() > v.ycor() - 15 and v1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            v.hideturtle()
            v1 = 1

       # Checks the bricks I and R
    if 184 > ball.xcor() > 104:
        if i.ycor() < ball.ycor() < i.ycor() + 15 and i1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            i.hideturtle()
            i1 = 1
        elif i.ycor() > ball.ycor() > i.ycor() - 15 and i1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            i.hideturtle()
            i1 = 1

        if r.ycor() < ball.ycor() < r.ycor() + 15 and r1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            r.hideturtle()
            r1 = 1
        elif r.ycor() > ball.ycor() > r.ycor() - 15 and r1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            r.hideturtle()
            r1 = 1

       # Checks the bricks E, N, and W
    if 274 > ball.xcor() > 154:
        if e.ycor() < ball.ycor() < e.ycor() + 15 and e1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            e.hideturtle()
            e1 = 1
        if e.ycor() > ball.ycor() > e.ycor() - 15 and e1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            e.hideturtle()
            e1 = 1

        if n.ycor() < ball.ycor() < n.ycor() + 15 and n1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            n.hideturtle()
            n1 = 1
        if n.ycor() > ball.ycor() > n.ycor() - 15 and n1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            n.hideturtle()
            n1 = 1

        if w.ycor() < ball.ycor() < w.ycor() + 15 and w1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            w.hideturtle()
            w1 = 1
        if w.ycor() > ball.ycor() > w.ycor() - 15 and w1 == 0:
            ball.sety(ball.ycor())
            ball.dy *= -1
            w.hideturtle()
            w1 = 1

if life == 0:
    lives.clear()
    lives.write("You Lost!", align='center', font=("Courier", 20, "bold"))
    sleep(4)
    quit()

elif win == 23:
    lives.clear()
    lives.write("You Won!", align='center', font=("Courier", 20, "bold"))
    sleep(4)
    quit()
