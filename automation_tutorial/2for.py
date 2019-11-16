import turtle

# for name in "John", "Sam", "Jill":  # for loop with strings
#     print("Hello " + name)
#
# for i in range(10):  # for loop with range of numbers, range(start, end, step)
#     print(i)
#
#
# total = 0
# for i in 5, 7, 11, 13:
#     print(i)
#     total = total + i
# print(total)
#
# for _ in range(10):  # no 'i' needed, don't care to use it and don't need the numbers...
#     print("Hello!")


# for drink in list_of_beverages:  # can print array filled with strings
#     print("Would you like a " + drink + "?")

for i in range(10):  # can let the turtle do multiple steps
    turtle.forward(15)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()

for _ in range(4):  # can leave i out...
    turtle.forward(100)
    turtle.left(90)


turtle.exitonclick()
