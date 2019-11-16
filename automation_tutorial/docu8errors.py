

8. Errors and Exceptions
two distinguishable kinds of errors: syntax errors and exceptions.

# 8.1. Syntax Errors
# 8.2. Exceptions
# Even if a statement or expression is syntactically correct,
# it may cause an error when an attempt is made to execute it.
# Errors detected during execution are called exceptions
# types of exceptions:
# ZeroDivisionError
# NameError
# TypeError

# 8.3. Handling Exceptions
# possible to write programs that handle selected exceptions, zb:
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

# A try statement may have more than one except clause
# except (RuntimeError, TypeError, NameError):
#    pass

# A class in an except clause is compatible with an exception if it is the same class or a base class thereof
# class B(Exception):
#     pass
#
# class C(B):
#     pass
#
# class D(C):
#     pass
#
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")


# 8.4. Raising Exceptions
# The raise statement allows the programmer to force a specified exception to occur
#
# 8.5. User-defined Exceptions
# Programs may name their own exceptions by creating a new exception class (see Classes for more about Python classes).
# Exceptions should typically be derived from the Exception class, either directly or indirectly.
#
# 8.6. Defining Clean-up Actions
# The try statement has another optional clause which is intended to define
# clean-up actions that must be executed under all circumstances.

# 8.7. Predefined Clean-up Actions
# Some objects define standard clean-up actions to be undertaken when the object is no longer needed,
# regardless of whether or not the operation using the object succeeded or failed
# for line in open("myfile.txt"):
#     print(line, end="")
# this code is that it leaves the file open for an indeterminate amount of time
# after this part of the code has finished executing
# with statement, objects are always cleaned up promptly and correctly
# with open("myfile.txt") as f:
#     for line in f:
#         print(line, end="")














