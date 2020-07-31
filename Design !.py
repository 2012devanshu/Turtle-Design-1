
__author__ : "@rockdevu"

# Turtle Design - 1

import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('white')
c = 0
while True:
    for i in range(4):
        t.forward(89)
        t.right(90)
    t.right(5)
    c+=1
    if c>=72:
        break

t.hideturtle()
turtle.done()
