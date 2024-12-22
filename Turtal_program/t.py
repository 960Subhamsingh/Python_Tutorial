import turtle
fore = 1
t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)
while True:
    t.forward(fore)
    t.color('red')
    t.left(13)
    t.left(1)
    fore +=1
    t.forward(fore)
    t.color("blue")
    t.right(70)
turtle.close