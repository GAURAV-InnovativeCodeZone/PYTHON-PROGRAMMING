from turtle import Turtle, Screen
import time

# Set up the screen
screen = Screen()
screen.bgcolor('midnightblue')
screen.title("Radiant Sun Animation")
screen.tracer(0)  # Disable auto-update for smooth animation

# Create sun turtle
sun = Turtle()
sun.hideturtle()
sun.speed(0)
sun.width(3)

# Animation colors
colors = ['gold', 'orange', 'crimson', 'darkorange', 'yellow']

# Animation loop
for i in range(100):
    sun.clear()
    sun.begin_fill()
    sun.color(colors[i%5], 'lemonchiffon')
    
    # Draw sun rays
    for _ in range(36):
        sun.forward(300 - i*2)  # Gradually shrink
        sun.left(170)
        if abs(sun.pos()) < 1:
            break
    
    sun.end_fill()
    screen.update()
    time.sleep(0.05)

screen.mainloop()
