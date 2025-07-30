       # create sun animation

from turtle import *
import turtle
t=Turtle()
s=Screen()
s.bgcolor('black')
color('red', 'yellow')
t.hideturtle()

begin_fill()
while True:
    t.speed(0)
    fd(350)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()

done()