#without loop
import turtle
s=turtle.Turtle()
s.forward(300)
s.left(90)
s.forward(300)
s.left(90)
s.forward(300)
s.left(90)
s.forward(300)
s.left(90)

s.hideturtle() #it will hide the small dark triangle
s.showturtle() # it will show the small dark triangle

#With loop

import turtle
s=turtle.Turtle()

for i in range(4):
    s.forward(300)
    s.left(90)
