
# 10. Brief Tour of the Standard Library
# 10.1. Operating System Interface
# os module for operating system interction
# import os
# print(os.getcwd())
# os.chdir('/server/assesslogon')  # changes current working directory
# os.system('mkdir today')  # runs command mkdir in the system shell
# dir(os)  # returns a list of all module funcitons
# help(os)  # returns an extensive manual page created from the modules docstrings..

# # For daily file and directory management tasks use shutil module
# import shutil
# shutil.copyfile('data.db','archive.db')
# shutil.move('/build/executive/funk','installdir')


# 10.2. File Wildcards
# glob module, make file lists from directory wildcard searches
# import glob
# glob.glob('*.py')
# ['primes.py', 'random.py', 'quote.py']


# 10.3. Command Line Arguments
# Common utility scripts often need to process command line arguments.
# These arguments are stored in the sys modules argv attribute as a list.
# import sys
# print(sys.argv)
# ['demo.py', 'one', 'two', 'three']

# use argparse module to process command line arguments
# import argparse
# from getpass import getuser
# parser = argparse.ArgumentParser(description='An argparse example.')
# parser.add_argument('name', nargs='?', default=getuser(), help='The name of someone to greet.')
# parser.add_argument('--verbose', '-v', action='count')
# args = parser.parse_args()
# greeting = ["Hi", "Hello", "Greetings! its very nice to meet you"][args.verbose % 3]
# print(f'{greeting}, {args.name}')
# if not args.verbose:
#     print('Try running this again with multiple "-v" flags!')


# 10.4. Error Output Redirection and Program Termination
# most direct way to terminate a script is to use sys.exit().


# 10.5. String Pattern Matching
# re module has tools for string processing
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

# for simple stuff, use string methods like
print('tea for too'.replace('too', 'two'))


# 10.6. Mathematics
import math  # for floating point math
print(math.cos(math.pi / 4))
print(math.log(1024, 2))

import random  # tools for random selections
print(random.choice(['apple', 'pear', 'banana']))
gaga = random.sample(range(100), 10) # sampling without replacement
baba = sorted(gaga)
print(baba)
print(random.random())  # random float
print(random.randrange(6))  # random integer chosen from range 6

# statstics module for basic statistics
import numpy
data = [1.25, 0.25, 0.5, 1.25, 100.00]
print data
a = numpy.mean(data)
a2 = numpy.median(data)
a3 = numpy.var(data)
b = numpy.mean(baba)
b2 = numpy.median(baba)
b3 = numpy.var(baba)
print(a, a2, a3)
print(b, b2, b3)


# 10.7. Internet Access
# urllib.request for retreiving dta from URLs and
# smtplib for sending mail
#     from urllib.request import urlopen
# with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
#     for line in response:
#         line = line.decode('utf-8')  # Decoding the binary data to text.
#         if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#             print(line)
#
#
# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
#                 """To: jcaesar@example.org
#                 From: soothsayer@example.org
#
#                 Beware the Ides of March.
#                 """)
# server.quit()


# 10.8. Dates and Times w datetime module
# dates are easily constructed and formatted
from datetime import date
now = date.today()
now
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
print 'tom age in years', age.days/365
print 'tom age in days', age.days


# 10.9. Data Compression
# compression formats modules including: zlib, gzip, bz2, lzma, zipfile and tarfile

# import zlib
# s = b'witch which has which witches wrist watch'
# len(s)
# t = zlib.compress(s)
# len(t)
# zlib.decompress(t)
# zlib.crc32(s)

# 10.10. Performance Measurement w timeit
# from timeit import Timer
# Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
# Timer('a,b = b,a', 'a=1; b=2').timeit()
# profile and pstats modules provide tools for identifying
# time critical sections in larger blocks of code.


# 10.11. Quality Control w doctest
# def average(values):
#     """Computes the arithmetic mean of a list of numbers.
#
#     >>> print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)
#
# import doctest
# doctest.testmod()   # automatically validate the embedded tests
# unittest more comprehensive than doctest


# 10.12. Batteries Included
# Python has a batteries included philosophy
















