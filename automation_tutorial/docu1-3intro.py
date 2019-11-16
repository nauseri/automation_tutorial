from fractions import Fraction
from decimal import Decimal

the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")

#comments
# this is the first comment
spam = 1  # and this is the second comment
# ... and now a third!
text = "# This is not a comment because it's inside quotes."
print(text)



# SIMPLE MATH
#math operations
a = 2 + 2
b = 50 - 5*6
c = (51.0 - 5*6) / 4
d = 12 % 5 # division always returns a floating point number
e = a**d**d
print(a, b, c, d, e)

#n  # try to access an undefined variable
tax = 12.5 / 100
price = 100.50
mua = price * tax
print(mua)

#fractions
gag = Fraction(16, -10)
pla = Fraction(Decimal('8.5'))
no = Fraction(123)
print(gag, pla, no)


# STRINGS
print('spam eggs')  # single quotes
print('doesn\'t')  # use \' to escape the single quote...
print("doesn't")  # ...or use double quotes instead
print('"Yes," they said.')
s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output
print(s)  # with print(), \n produces a new line

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

print("""this is for strings that are waaaay to long.......................................................................................""")

# concatenation, putting strings together
print(3*'noi' + 'loool')
text = ('Put several strings within parentheses'  'to have them joined together.')
print(text)

# strings can be indexed (subscripted)
word = 'python'
print(word[2])  # starts at zero!
print(word[-1])  # last character
print(word[-2])  # second-last character
# slicing gives me substrings
print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
# This makes sure that s[:i] + s[i:] is always equal to s:
print(word[:2] + word[2:])
print(word[:2])  # character from the beginning to position 2 (excluded)
print(word[4:])  # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end

# think of the indices as pointing between characters
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#  -6  -5  -4  -3  -2  -1

# For non-negative indices, the length of a slice is the difference of the indices
ars = len(word[1:3])  # len for length, results here in 2
print(ars)
# out of range slice indexes works...
print(word[4:100])

# python strings are immutable, means that they cannot be changed
# if another string is needed, must create a new one
print('g'+word[1:])

# LISTS are mutable, content can be changed
# compound data type, groups together other values. can contain different types but usually has the same in it
listii = [1, 3, 5, 23, 3, 58]
print(listii)
# can be indexed and sliced
print(listii[-2])  # indexing
print(listii[2:5])  # slicing
print(listii[-3:])
# also supports concatenation
print(listii + [33, 4, 55456,  34, 251])

listii[3:5] = [36, 5, 9]  # can replace values in a list, is mutable
print(listii)
# can add items with append()
listii.append(100)
print(listii)
print(len(listii))
# list nesting possible
abba = [21, 22, 23]
alla = [45, 46, 47]
cc = [abba, alla]
print(cc)
print(cc[0])
print(cc[1][0])



# First Steps Towards Programming
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1 # multiple assignments, initialization
while a < 10:  # while loop, stops until condition is met, == equal, != not equal etc
    print(a)  # indentation important to group statements!
    a, b = b, a+b

texto = 'the value of a is'
print(texto, a)



