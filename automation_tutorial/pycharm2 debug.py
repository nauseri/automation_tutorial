

# link:
# https://www.youtube.com/watch?v=sRGpvbhOhQs


# how to do debugging


# add a break point to check out the code -> red dot next to the numbers on the side
# push debug, the green insect on the side
# this will run the code until the red dot

# window debugger below, see variables with value until that red dot
# also in the console, the variables
# are displayed in the same line as where the variable is

# can add smth to watch, next to the variables down below, press the + button
# wrote: str(ans) == result and the answer to that is False
# can check stuff there without needing to write it here in the codespace
# with - the watch can be deleted
# in debugger, to continue from red dot, press the green resume programm (F9) button
# and red round circle to stop debugging

# multiple breakpoints possible
# next to debugger and console, there are buttons, can be used to go through code one by one
# step into my code, step over etc
# small calculator looking icon, evaluate expression, can try out stuff without needing to print them out

# frames in window below shows different views of codespace


import random


def numberos():
    run = True
    num1 = random.randint(1, 11)
    num2 = random.randint(1, 11)
    result = num1 * num2
    while run:
        anso = str(input('what is ' + str(num1) + 'x' + str(num2) + '? '))

        if anso.isdigit():
            if int(anso) == result:
                print('correct')
                run = False
            else:
                print('wrong: try again')
        else:
            print('the answer must be a positive number, try again')


# global vars

times = 10

for x in range(times):
    numberos()




















