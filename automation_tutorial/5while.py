import turtle

# # while statement
# word = ''
# sentence = ''
# print('Please enter some words.')
# print('Include a period (.) when you are finished.')
# while '.' not in word:
#     word = input('next word: ')
#     sentence = sentence + ' ' + word
# print()
# print('Aha! You said:')
# print(sentence)
# --------------------------------------------------------------------------------------


# def forward(distance):  # implementing while statement to return turtle to original location
#     while distance > 0:
#         if turtle.distance(0, 0) > 100:   # turtle.distance(0, 0)  # Returns turtle distance from origin
#             angle = turtle.towards(0, 0)  # turtle.towards(0, 0)  # Returns the angle to get back to origin (0, 0)
#             turtle.setheading(angle)   # turtle.setheading(angle)  # Directly sets the turtle’s direction
#         turtle.forward(1)
#         distance = distance - 1
#
#
# forward(350)
# --------------------------------------------------------------------------------------


def spiral(stop):  # turns turtle in a spiral until condition is met and then stops
    x = turtle.xcor()
    y = turtle.ycor()
    move = 1
    while True:
        turtle.forward(move)
        turtle.left(30)
        move += 0.5
        if turtle.distance(x, y) > stop:
            break


spiral(100)

turtle.exitonclick()
