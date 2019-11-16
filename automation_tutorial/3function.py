import turtle


# def line_without_moving():  # def for defining a function, no value needed in () but useful
#     turtle.forward(50)
#     turtle.backward(50)
#
#
# def star_arm():
#     line_without_moving()
#     turtle.right(360 / 5)
#
#
# for _ in range(5):
#     star_arm()
# ---------------------------------------------------------------------------


# def tilted_square():
#     turtle.left(20)     # now we can change the angle only here
#     for _ in range(4):
#         turtle.forward(50)
#         turtle.left(90)
#
#
# tilted_square()
# tilted_square()
# tilted_square()
#
# # bonus: you could have a separate function for drawing a square,
# # which might be useful later:
#
#
# def square():
#     for _ in range(4):
#         turtle.forward(50)
#         turtle.left(90)
#
#
# def tilted_square():
#     turtle.left(20)
#     square()

# etc

# --------------------------------------------------------------------------------------


# def move(length, nr):  # here function with smth in (), returns hexagon
#     for _ in range(nr):
#         turtle.left(360/nr)
#         turtle.forward(length)
#
#
# move(50, 8)  # output of the function

# --------------------------------------------------------------------------------------
lines = 6


def move(lengths):
    for ii in range(lines):
        turtle.left(lengths)
        turtle.forward(lengths)


def adjust():
    turtle.right(60)
    turtle.forward(50)


for _ in range(6):
    move(50)
    adjust()


turtle.exitonclick()
