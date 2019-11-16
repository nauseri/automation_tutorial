

# 9. Classes
# bundles data and functionality together
# they are created at runtime, and can be modified further after creation.
# classes create new type of object with new instances, with instances having attributes
# Class instances can also have methods (defined by its class) for modifying its state.

# 9.1. A Word About Names and Objects
# 9.2. Python Scopes and Namespaces
# A namespace is a mapping from names to objects
# Examples of namespaces are:
# the set of built-in names (containing functions such as abs(),
# and built-in exception names);
# the global names in a module; and
# the local names in a function invocation
# there is absolutely no relation between names in different namespaces,
# can use same name in different modules, since modulename.attribute... cant be confused
# but better use different names...
# attribute for any name following a dot

# A scope is a textual region of a Python program where a namespace is directly accessible.
# Directly accessible here means that an unqualified reference to a name attempts to find the name in the namespace.

# This is an example demonstrating how to reference the different scopes and namespaces,
# and how global and nonlocal affect variable binding:


# 9.2.1. Scopes and Namespaces Example

# def scope_test():
#     def do_local():
#         spam = "local spam"
#
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#
#     def do_global():
#         global spam
#         spam = "global spam"
#
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
#
# scope_test()
# print("In global scope:", spam)
# The output of the example code is:
#
# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam


# 9.3. A First Look at Classes
# 9.3.1. Class Definition Syntax
# Class definitions, like function definitions (def statements) must be executed before they have any effect.
# class ClassName:
#     <statement-1>
#     .
#     <statement-N>
# statements inside a class definition will usually be function definitions


# 9.3.2. Class Objects
# Class objects support two kinds of operations:
# attribute references and instantiation.
# Attribute references: obj.name
# class MyClass:
#     """A simple example class"""
#     i = 12345
#
#     def f(self):
#         return 'hello world'
# MyClass.i and MyClass.f are valid attribute references, returning an integer and a function object, respectively
#
# Class instantiation uses function notation. Just pretend that the class object is a parameterless function
# that returns a new instance of the class. For example (assuming the above class):
#     x = MyClass()
# creates a new instance of the class and assigns this object to the local variable x.
# create objects with instances customized to a specific initial state
# def __init__(self):
#     self.data = []
# x = MyClass()

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)


# 9.3.3. Instance Objects
# only operations understood by instance objects are attribute references
# valid attribute names: data attributes and methods
# example, if x is the instance of MyClass created above,
# data attributes: the following piece of code will print the value 16, without leaving a trace:
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

# instance attribute reference: method
# A method is a function that belongs to an object

# 9.3.4. Method Objects
# Usually, a method is called right after it is bound
# x.f()
# x.f() is exactly equivalent to MyClass.f(x). In general,
# calling a method with a list of n arguments is equivalent to calling the corresponding function with
# an argument list that is created by inserting the methods instance object before the first argument.

# 9.3.5. Class and Instance Variables
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)  # shared by all dogs
print(e.kind)  # shared by all dogs
print(d.name)  # unique to d
print(e.name)  # unique to e

# Correct design of the class should use an instance variable instead
# class Dog:
#
#     def __init__(self, name):
#         self.name = name
#         self.tricks = []    # creates a new empty list for each dog
#
#     def add_trick(self, trick):
#         self.tricks.append(trick)
#
#d = Dog('Fido')
#e = Dog('Buddy')
#d.add_trick('roll over')
#e.add_trick('play dead')
#print(d.tricks)
#print(e.tricks)


# 9.4. Random Remarks
# If the same attribute name occurs in both an instance and in a class,
# then attribute lookup prioritizes the instance
# give different names to different things and i should be good!!
# naming convention can save a lot of headaches

# Often, the first argument of a method is called self.
# This is nothing more than a convention: the name self has absolutely no special meaning to Python
# Methods may call other methods by using method attributes of the self argument
# class Bag:
#     def __init__(self):
#         self.data = []
#
#     def add(self, x):
#         self.data.append(x)
#
#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)

# Each value is an object, and therefore has a class (also called its type). It is stored as object.__class__.


# 9.5. Inheritance
# class DerivedClassName(BaseClassName):
#     <statement-1>
#     .
#     <statement-N>

# class DerivedClassName(modname.BaseClassName):  # when the base class is defined in another module
#     Derived classes may override methods of their base classes
# An overriding method in a derived class may in fact want to extend rather than
# simply replace the base class method of the same name.
# BaseClassName.methodname(self, arguments)


# 9.5.1. Multiple Inheritance
# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     .
#     <statement-N>


# 9.6. Private Variables
# convention that is followed by most Python code:
# a name prefixed with an underscore (e.g. _spam) should be treated as a
# non-public part of the API (whether it is a function, a method or a data member).
# it should be considered an implementation detail and
# subject to change without notice.

# Name mangling is helpful for letting subclasses override methods
# without breaking intraclass method calls. For example:
#
# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)
#
#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)
#
#     __update = update   # private copy of original update() method
#
# class MappingSubclass(Mapping):
#
#     def update(self, keys, values):
#         # provides new signature for update()
#         # but does not break __init__()
#         for item in zip(keys, values):
#             self.items_list.append(item)

# Note that the mangling rules are designed mostly to avoid accidents


# 9.7. Odds and Ends
# data type that bundles together a few named data items,
# use empty class definition
# class Employee:
#     pass
#
# john = Employee()  # Create an empty employee record
#
# # Fill the fields of the record
# john.name = 'John Doe'
# john.dept = 'computer lab'
# john.salary = 1000


# 9.8. Iterators
# most container objects can be looped over using a for statement
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
# for line in open("myfile.txt"):
#     print(line, end='')


# 9.9. Generators
# tools for creating iterators using yield statement to return data
def frontal(data):  # def reverse(data):
    for index in range(0, len(data), 1):  # for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in frontal('kamm'):  # for char in reverse('kamm'):
    print(char)

# features make it easy to create iterators with
# no more effort than writing a regular function.


# 9.10. Generator Expressions
# Some simple generators can be coded succinctly as expressions using a
# syntax similar to list comprehensions but with parentheses instead of square brackets.
print(sum(i*i for i in range(10)))  # sum of squares
xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))  # dot product

unique_words = set(word for line in page for word in line.split())
valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))  # ['f', 'l', 'o', 'g']








