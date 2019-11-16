
print("Hello world")  # how to print out stuff in terminal
(1 + 4) * 2
(239 + 588) ** 2  # exponent with **
# help()
# cd Desktop\Python_Exercises  # how to change directory

# -------------------------------------------------------------------
import turtle  # function for help to illustrate python stuff
turtle.forward(25)
turtle.left(30)
turtle.backward(1)
turtle.right(1)
turtle.shape("turtle")
turtle.forward(25)
turtle.exitonclick()
turtle.reset()
# turtle.width(...)  # how to change shape and color
# turtle.color(...)
# help(turtle.color)
# turtle.undo().
# -------------------------------------------------------------------
x = 5  # can add value or change turtle name and replace it...
turtle.forward(x)

timmy = turtle
timmy.forward(50)
timmy.left(90)
turtle.forward(50)
tilt = 20
turtle.left(tilt)
turtle.left(tilt)

turtle.exitonclick()

import math  # need to import package to use math functions

a = 10
b = 2

c = math.sqrt(a**2 + b**2)
print(c)
