

# lesson 7: for loop

print 'i am'
for i in range(5):
    print 'jameson ' + str(i)

total = 0
for ii in range(0, 101, 1):
    total = total + ii
    if total > 1000:
        break

print total



# lesson 8:
# build in functions in python: print, len(), input() etc
# modules: standard library that can be used: math, random, etc.
# they need to be imported with import ...

import random
b = 0
for i in range(3):
    a = random.randint(1, 10)
    print a
    b = b + a
print b

# import sys
# print 'hello'
# sys.exit()
# print 'will not print'

# third party modules can be imported with pip...
# in terminal, type: pip install pyperclip
import pyperclip
pyperclip.copy('hello there')
print pyperclip.paste()



# lesson 9: functions, non value and keyword arguments

def hello(name):
    print 'jallo ' + name + 'how ya doing'
    print 'your name has ' + str(len(name)) + ' letters in it'



print hello('bob')
print hello('alice')


def plusone(number):
    return number + 1

newnumber = plusone(3)
print newnumber

# keyword arguments to functions are usually for optional arguments
# the print function has keyword arguments end and sep...



# lesson 10: local and global scope

spam = 42  # is a global variable

def eggs():
    spam = 42  # local variable

# 1 code in a global scope cannot use any local variables
# 2 code in a local scope can access global variables
# 3 code in one functions local scope cannot use variables in another local scope
# 4 code in one functions local scope cannot use variables in any other local scope

def spam():
    global eggs  # turns eggs into a global variable and can be used locally
    eggs = 'hello'
    print eggs

eggs = 42
spam()
print(eggs)






