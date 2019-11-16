
# if statement
# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print('negative value changed to zero')
# elif x == 0:  # short form for else if
#     print('zero')
# elif x < 10:
#     print('single digit number')
# else:
#     print('more than 9')

# for statement, Pythons for statement iterates over
# the items of any sequence (a list or a string),
# in the order that they appear in the sequence

# for as string measurement
wordplay = ['bread', 'honey', 'ovomaltine']
for w in wordplay:
    print(w, len(w))

# loop over a copy of the collection or to create a new collection

# Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status

# range statement
for i in range(5):  # generates arithmetic progressions
    print(i)

for i in range(0, 10, 3):  # start included, end excluded, steps
    print(i)

# iterate over the indices of a sequence
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print(sum(range(4)))  # sums up the numbers in range, 0 - 3
print(list(range(4)))  #how to get a list from a range

# break and continue statement and else clauses on loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:  # the % operator returns the remainder of the division
            print(n, 'equals', x, '*', n//x)  # floor division discards the fractional part
            break
    else:  # loop statements may have a else statement!!
        print(n, 'is a prime number')  # loop fell through without finding a factor

for num in range(2, 10):
    if num % 2 == 0:
        print("Found EVEN number", num)
        continue  # continues with the next iteration of the loop
    print("Found A number", num)

# pass statement
# while True:
#     pass  # this does nothing, can be used as placeholder until code is ready...

# defining functions


def fib(m):  # create fibonacci function
    """Print a Fibonacci series up to m."""
    a, b = 0, 1
    while a < m:
        print(a)
        a, b = b, a+b  # this swappes numbers! from a to b and b to a


print(fib(20))


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # smth.smth calls a method for an object, ...
        # here it adds a new element to the end of a list
        a, b = b, a+b
    return result  # returns with a value from a function, ...
    # without this we would only get None as a result!
print(fib2(100))

# more defining functions
# def ask_ok(prompt, retries=4, reminder='Please try again!'):  # shows that multiple arguments can be used to define a function
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):  # in tests whether or not a sequence contains a certain value
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

#i = 5  # default values are evaluated at the point of function definition
# def f(arg=i):
#     print(arg)
# i = 6
# f()
# will print 5.

# default value evaluated only once, so mutable objects like a list will act weird...


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):  # fkt can be called with keyword arguments
    print("-- This parrot wouldn't", action)
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# positional and keyword argument
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

def cheeseshop(kind, *arguments, **keywords):  #smth about * and ** ...
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


print(cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch"))

# 4.7.3 special parameters
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):  # a function definition may look like this
#     -----------    ----------     ----------
#     |             |                  |
#     |        Positional or keyword   |
#     |                                - Keyword only
#     -- Positional only
# / and * are optional but needed if you want one of the three above
# arguments may be passed to a function by position or by keyword

# examples
# def standard_arg(arg):  # no restrictions on arguments
# print(arg)
# def pos_only_arg(arg, /):
#  print(arg)
# def kwd_only_arg(*, arg):
# print(arg)
# def combined_example(pos_only, /, standard, *, kwd_only):  # all calling conventions possible...
# print(pos_only, standard, kwd_only)

# recap, use case determines which parameters to use in the function definition
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):


# 4.7.4. Arbitrary Argument Lists...
# 4.7.5. Unpacking Argument Lists
print(list(range(3, 6)))   # normal call with separate arguments
args = [3, 6]
print(list(range(*args)))  # call with arguments unpacked from a list, need a star

# 4.7.6. Lambda Expressions, anonymous function with lambda as keyword
# used for functional programming
def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(1))

# 4.7.7. Documentation Strings, how to conventions
# 4.7.8. Function Annotations

# 4.8. Intermezzo: Coding Style, guide PEP 8...
# use for space indentation and no tabs
# wrap lines up to 79 characters
# blank lines to separate stuff
# name funcitons and classes consistently
# use UpperCamelCase for classes and lowercase_with_underscores for functions and methods
# always use self as the name for the first method argument




















