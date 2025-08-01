#Imported turtle
import turtle

#set the turtle object
t=turtle.Turtle()
scr=t.getscreen()
scr.bgcolor("Light Blue")

#Drawing the face of the dog
t.pencolor("tan1")
t.color("tan1")
t.pensize(3)
t.penup()
t.setheading(90)
t.goto(30,-30)
t.pendown()
t.begin_fill()
t.circle(45,180)
t.right(90)
t.goto(-45,-30)
t.circle(35,190)
t.setheading(0)
t.forward(55)
t.penup()
t.setheading(0)
t.pendown()
t.circle(35,170)
t.penup()
t.end_fill()

#Create the tongue of the dog
t.pencolor("DeepPink1")
t.color("Pink")
t.setheading(270)
t.goto(-10,-90)
t.right(60)
t.pendown()
t.begin_fill()
t.forward(15)
t.left(60)
t.forward(10)
t.circle(10,180)
t.forward(10)
t.left(60)
t.forward(15)
t.end_fill()

#line on the tongue
t.pensize(1)
t.pencolor("DeepPink")
t.goto(-13,-90)
t.setheading(270)
t.forward(17)
t.circle(4,180)
t.penup()
t.left(90)
t.forward(8)
t.goto(-13,-107)
t.setheading(270)
t.left(180)
t.pendown()
t.circle(4,-180)

#right ear
t.penup()
t.goto(42,-45)
t.pencolor("black")
t.color("sienna")
t.setheading(0)
t.pendown()
t.begin_fill()
t.forward(10)
t.left(60)
t.circle(35,145)
t.end_fill()

#left ear
t.penup()
t.goto(-70,-45)
t.pendown()
t.setheading(180)
t.begin_fill()
t.forward(10)
t.left(-240)
t.circle(35,-145)
t.end_fill()
t.penup()


#eyes
t.pencolor("black")
t.color("black")
t.goto(-5,-45)
t.setheading(270)
t.pendown()
t.begin_fill()
t.circle(10,180)
t.forward(5)
t.circle(10,180)
t.forward(5)
t.end_fill()
t.penup()

t.pencolor("black")
t.color("black")
t.goto(-45,-45)
t.setheading(270)
t.pendown()
t.begin_fill()
t.circle(10,180)
t.forward(5)
t.circle(10,180)
t.forward(5)
t.end_fill()
t.penup()

# Inner white dots in the eye
t.color("white")
t.goto(-2,-44)
t.begin_fill()
t.circle(6)
t.end_fill()

t.color("white")
t.goto(-40,-44)
t.begin_fill()
t.circle(6)
t.end_fill()

#Nose of the dog
t.color("black")
t.goto(-25,-75)
t.begin_fill()
t.circle(10)
t.end_fill()
t.goto(-14,-73)
t.color("white")
t.begin_fill()
t.circle(2)
t.end_fill()
t.goto(-20,-73)
t.color("white")
t.begin_fill()
t.circle(2)
t.end_fill()
t.goto(-17,-77)
t.color("white")
t.begin_fill()
t.circle(2)
t.end_fill()
t.hideturtle()
turtle.done()