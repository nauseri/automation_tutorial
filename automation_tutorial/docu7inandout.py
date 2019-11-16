


# 7. Input and Output
# output either printed or written to a file for future use
#
# 7.1. Fancier Output Formatting
# write values: expression statements, print() funciton or write()
# output format
# To use formatted string literals, begin a string with f
# year = 2016
# event = 'Referendum'
# print(f"Results of the {year} {event}")

# The str.format() method of strings requires more manual effort
# Finally, you can do all the string handling yourself by using string slicing and concatenation operations to create any layout you can imagine.
# want a quick display of some variables for debugging purposes, you can convert any value to a string with the repr() or str() functions
# s = 'Hello, world.'
# str(s)
# 'Hello, world.'
# repr(s)
# "'Hello, world.'"
# str(1/7)
# '0.14285714285714285'
# x = 10 * 3.25
# y = 200 * 200
# s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
# print(s)
# The value of x is 32.5, and y is 40000...
# # The repr() of a string adds string quotes and backslashes:
# hello = 'hello, world\n'
# hellos = repr(hello)
# print(hellos)
# 'hello, world\n'
# # The argument to repr() may be any Python object:
# repr((x, y, ('spam', 'eggs')))
# "(32.5, 40000, ('spam', 'eggs'))"


# 7.1.1. Formatted String Literals
# let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}
# import math
# print(f'The value of pi is approximately {math.pi:.3f}.')
# Passing an integer after the ':' will cause that field to be a minimum number of characters wide
# for name, phone in table.items():
#     print(f'{name:10} ==> {phone:10d}')

# Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), '!s' applies str(), and '!r' applies repr()
# animals = 'eels'
# print(f'My hovercraft is full of {animals}.')
# My hovercraft is full of eels.
# print(f'My hovercraft is full of {animals!r}.')
# My hovercraft is full of 'eels'.


# 7.1.2. The String format() Method
# Basic usage of the str.format()
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
# This spam is absolutely horrible.

# Positional and keyword arguments can be arbitrarily combined
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
# The story of Bill, Manfred, and Georg.

# If you have a really long format string that you dont want to split up, it would be nice if you could reference the variables to be formatted by name instead of by position
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678
# same with the ** notation
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


# example, the following lines produce a tidily-aligned set of columns
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))  # d for Decimal Integer. Outputs the number in base 10.

# for overview of str.format() see format string snytax

# 7.1.4. Old string formatting
# The % operator can also be used for string formatting
import math
print('The value of pi is approximately %5.3f.' % math.pi)
# The value of pi is approximately 3.142.


# 7.2. Reading and Writing Files
# open() returns a file object, and is most commonly used with two arguments: open(filename, mode).
# f = open('workfile', 'w')
# mode: r for reading, w for writing, a opens the file for appending, r+ opens the file for reading and writing
# mode argument optional r will be assumed if omitted

# Normally, files are opened in text mode, that means, you read and write strings from and to the file, which are encoded in a specific encoding
#
# It is good practice to use the with keyword when dealing with file objects
# with open('workfile') as f: read_data = f.read()
# # We can check that the file has been automatically closed.
# f.closed
# True
# If you’re not using the with keyword, then you should call f.close() to close the file and immediately free up any system resources used by it.
# ... If you don’t explicitly close a file, Python’s garbage collector will eventually destroy the
# ... object and close the open file for you, but the file may stay open for a while


# 7.2.1. Methods of File Objects
# The rest of the examples in this section will assume that a file object called f has already been created.
# To read a file’s contents, call f.read(size)
# f.read(size)
# 'This is the entire file.\n'
# f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and
# ... is only omitted on the last line of the file if the file doesn’t end in a newline.
# f.readline()
# 'This is the first line of the file.\n'

# For reading lines from a file, you can loop over the file object
# for line in f:
#     print(line, end='')

# To change the file objects position, use f.seek(offset, whence)
# f = open('workfile', 'rb+')
# f.write(b'0123456789abcdef')


# 7.2.2. Saving structured data with json
#
# Rather than having users constantly writing and debugging code to save complicated data types to files,
# Python allows you to use the popular data interchange format called JSON (JavaScript Object Notation).
# The standard module called json can take Python data hierarchies, and convert them to string representations;
# this process is called serializing. Reconstructing the data from the string representation is called deserializing.
# Between serializing and deserializing, the string representing the object may have been stored in a file or data,
# or sent over a network connection to some distant machine.

# If you have an object x, you can view its JSON string representation with a simple line of code:
# import json
# json.dumps([1, 'simple', 'list'])
# dump(), simply serializes the object to a text file.
# So if f is a text file object opened for writing, we can do this:
# json.dump(x, f)
# decode the object again
# x = json.load(f)
# can handle lists and dictionaries, but serializing arbitrary class instances in JSON requires a bit of extra effort.
# The reference for the json module contains an explanation of this.

















