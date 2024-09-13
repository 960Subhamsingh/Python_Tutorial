import turtle
t = turtle.Turtle()
side = 50

for i in range(100):
    t.forward(side)
    t.right(90)
    side = side-2

import turtle
bob = turtle.Turtle()
bob.speed(0)
def c():
    for i in range(360):
        bob.forward(i)
        bob.left(120)
c()