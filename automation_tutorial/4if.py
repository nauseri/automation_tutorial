import turtle

# condition = True
# if condition:
#     print("condition met")
#
# if not condition:
#     print("condition not met")
#
# direction = -30
# if direction > 0:
#     turtle.forward(direction)
# else:
#     turtle.left(180)
#     turtle.forward(-direction)
#
# my_variable = "       I Am Capitalised"
# print(my_variable)
# my_stripped = my_variable.strip()  # .strip() removes whitespace
# print(my_stripped)
# my_lower = my_variable.lower()  # .lower() makes everything lower-case
# print(my_lower)

# ----------------------------------------------------------------------------------
#a = 5
#b = 50
#c = 50

def move():
    direction = input("Go left or right?").strip().lower()  # strip removes whitespace nad lower makes all lower case
    if direction == "left":
        for i in range(5):
            turtle.left(50)
            turtle.forward(50)
    if direction == "right":
        for i in range(5):
            turtle.right(50)
            turtle.forward(50)


move()

turtle.exitonclick()
