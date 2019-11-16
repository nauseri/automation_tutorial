# # 5.1 list methods
# list.append(x) Add an item to the end of the list
# list.extend(iterable) Extend the list by appending all the items from the iterable.
# list.insert(i, x) Insert an item at a given position.
# list.remove(x)
# list.pop([i])
# list.clear()
# list.index(x[, start[, end]])
# list.count(x)
# list.sort(key=None, reverse=False)
# list.reverse()
# list.copy()


homework = [11, 3, 9, 6, 4, 8, 3]
peta = homework.pop(3)
print(peta)  # pops that item out of the list and returns it for
print(homework)

print(homework.index(3, 0, 5))  # Return zero-based index in the list of the ...
# first item whose value is equal to x
print(homework.count(3))

homework.sort()
print(homework)

# some methods that only modify the list have no return value printed
# they return the default None
# This is a design principle for all mutable data structures in Python

jalla = ['gurke', 'apfel', 'orange', 'citrone', 'schoggi']
jalla.sort()
print(jalla)

homework.reverse()
print(homework)

# 5.1.1. Using Lists as Stacks
# with append add smth and with pop remove smth from a list (=stack), last in first out
# 5.1.2. Using Lists as Queues, first in first out
# is inefficient, better use collections.deque
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.popleft()
print(queue)

# 5.1.3. List Comprehensions, concise way to create lists by creating a new list...
# resulting from evaluating the expressin in the context of for and if cluases which follow
squares = []  # bad way to do things, overwrites variables
for x in range(10):
    squares.append(x ** 2)

print(squares)

# better way to do things
squares1 = list(map(lambda y: y ** 2, range(10)))
print(squares1)
# or
squares2 = [z ** 2 for z in range(10)]
print(squares2)

# more list comprehension example
aa = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(aa)
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
vario = [x * 2 for x in vec]
print(vario)

# 5.1.4. Nested List Comprehensions, list comp in a list comp etc...
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
mataa = [[row[i] for row in matrix] for i in range(4)]  # transpose of matrix
print(mataa)





# 5.2. The del statement, remove an item from a list given its index
# delete either one item, a slice or everything in a list or entire variables
a = [1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a)





# 5.3. Tuples is a Sequences data type
# use any type of value, zb string or integer...
# tuples are immutable but can contain mutable objects...
t = 12345, 54321, 'hello!'
u = t, (1, 2, 3, 4, 5)

empty = ()
singleton = 'hello',  # <-- note trailing comma, needs this to work
print(len(empty))
len(singleton)
print(singleton)
x, y, z = t  # called sequence unpacking. this needs enough variables on the left as items in the tuple
print(x)





# 5.4. Sets, unordered collection with no duplicate elements
# use curly braces or the set() to make sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)  # show that duplicates have been removed
print('orange' in basket)
print('crabgrass' in basket)
a = set('abracadabra')
print(a)  # unique letters in a
b = set('alacazam')
print(a - b)  # letters in a but not in b
print(a | b)  # letters in a or b or both
print(a & b)  # letters in both a and b
print(a ^ b)  # letters in a or b but not both
# set comprehension exists as well
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)





# 5.5. Dictionaries, are indexed by keys which are immutalbe
# a set of 'key: value' pairs with unique keys
# tuple can be used as keys in dictionaries but not lists
# main operation, storing and extracting a value with a key
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel))  # perform list() on a dict., get a list of all keys
print(sorted(tel))  # sorted() on a dict for sorting
print('guido' in tel)
print('jack' not in tel)
dici = dict([('sapo', 4139), ('guidi', 4127), ('jacko', 4098)])
print(dici)
# dict comprehensions
oho = {x: x**2 for x in (2, 4, 6)}
print(oho)
whato = dict(sapi=41, guid=47, jac=98)  # use this method when keys are simple strings, a bit easier...
print(whato)





# 5.6. Looping Techniques
# looping through dictionary, get key value pair with items()
sushi = {'tuna': 12, 'salmon': 8, 'eel': 6}
for a, b in sushi.items():
    print(a, b)
# looping through a sequence, get index position and value
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# loop over two or more sequences with zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
# reverse looping through a sequence
for i in reversed(range(1, 10, 2)):
    print(i)
# loop over a sequence in sorted order
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
# better to create a new list when looping
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)





# 5.7. More on Conditions
# comparison: in and not it to see if value in sequence
# is and is not compare objects, for mutable objects like lists
# comparison chaining possible: a < b == c
# boolean operators for comparison (A and (not B)) or C, parenthesis show priority





# 5.8. Comparing Sequences and Other Types
# Sequence objects typically may be compared to other objects with the same sequence type
# comparison uses lexicographical ordering
# (1, 2, 3)              < (1, 2, 4)
# [1, 2, 3]              < [1, 2, 4]
# 'ABC' < 'C' < 'Pascal' < 'Python'
# (1, 2, 3, 4)           < (1, 2, 4)
# (1, 2)                 < (1, 2, -1)
# (1, 2, 3)             == (1.0, 2.0, 3.0)
# (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

















