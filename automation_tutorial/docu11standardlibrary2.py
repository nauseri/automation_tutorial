

# 11. Brief Tour of the Standard Library Part II
# covers more advanced modules


# 11.1. Output Formatting
# reprlib for abbreviated displays ....
# pprint for nice printing
import textwrap  # textwrap formats paragraphs to fit to screen
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=60))
# The locale module accesses a database of culture specific data formats
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')

conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
print locale.format("%d", x, grouping=True)
print locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True)


# 11.2. Templating
# string w Template
# from string import Template
# t = Template('${village}folk send $$10 to $cause.')
# t.substitute(village='Nottingham', cause='the ditch fund')


# 11.3. Working with Binary Data Record LayoutsThe struct module provides pack() and
# unpack() functions for working with variable length binary record formats.
# 11.4. Multi-threading
# Threading is a technique for decoupling tasks which are not sequentially dependent.
# 11.5. Logging

# 11.6. Weak References
# Python does automatic memory management (reference counting for most objects and
# garbage collection to eliminate cycles). The memory is freed shortly after the
# last reference to it has been eliminated.
# The weakref module provides tools for tracking objects without creating a reference.
# Typical applications include caching objects that are expensive to create

# 11.7. Tools for Working with Lists
# The array module provides an array() object that is like a list that stores only
# homogeneous data and stores it more compactly. The following example shows an array of numbers
# stored as two byte unsigned binary numbers (typecode "H") rather than the usual 16 bytes per entry
# for regular lists of Python int objects:
# from array import array
# a = array('H', [4000, 10, 700, 22222])
# sum(a)
# a[1:3]
# collection module with deque(), faster appends and pops from left side
# from collections import deque
# d = deque(["task1", "task2", "task3"])
# d.append("task4")
# print("Handling", d.popleft())

# bisect module w fkt for manipulating sorted lists
# import bisect
# scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
# bisect.insort(scores, (300, 'ruby'))
# scores

# The heapq module provides functions for implementing heaps based on regular lists.


# 11.8. Decimal Floating Point Arithmetic
# The decimal module offers a Decimal datatype for decimal floating point arithmetic.
# for more precision and control compared to binary floating point
from decimal import *
print round(Decimal('0.70') * Decimal('1.05'), 2)
print round(.70 * 1.05, 2)

# Exact representation enables the Decimal class to perform modulo calculations
# and equality tests that are unsuitable for binary floating point:
Decimal('1.00') % Decimal('.10')
1.00 % 0.10
print sum([Decimal('0.1')]*10) == Decimal('1.0')
print sum([0.1]*10) == 1.0
























