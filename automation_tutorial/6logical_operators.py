import turtle

# x = False
# if not x:  # if condition is not met...
#     print("condition met")
# else:
#     print("condition not met")
# # ---------------------------------------------------
#
#
# def stealthed_forward(distance):  # function returns true if turtle is drawing...
#     if not turtle.isdown():  # not is a logical operator
#         turtle.forward(distance)
#
#
# stealthed_forward(100)
#
# # ---------------------------------------------------
# if 1 < 2 and 4 > 2:  # and, or statements
#     print("condition met")
#
# if 1 > 2 and 4 < 10:
#     print("condition not met")
#
# if 4 < 10 or 1 < 2:
#     print("condition met")
# ---------------------------------------------------
import math  # need to import package to use math functions


def spiral(x, y):  # turns turtle in a spiral until condition is met and then stop
    xx = turtle.xcor()
    yy = turtle.ycor()
    move = 1
    while True:
        turtle.forward(move)
        turtle.left(90)
        move += 2
        c = math.sqrt(move ** 2 + move ** 2)
        if turtle.distance(xx, yy) > x or turtle.distance(xx, yy) > y:
            turtle.setheading(turtle.towards(0, 0))
            turtle.forward(c/2)
            break


spiral(100, 100)
# ---------------------------------------------------------------------------


# def forward(distance):
#     while distance > 0:
#         if (turtle.xcor() > 100
#             or turtle.xcor() < -100
#             or turtle.ycor() > 100
#             or turtle.ycor() < -100):
#             turtle.setheading(turtle.towards(0,0))
#         turtle.forward(1)
#         distance = distance - 1
#
# forward(120)


turtle.exitonclick()
