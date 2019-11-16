

# lesson 11: how to handle error or exception
# use try and except to forgo error messages
# this procedure is called input validation

# def div42(divi):
#     try:
#         return 42 / divi
#     except ZeroDivisionError:
#         print 'Error: you tried to divide by zero'
#
# print div42(2)
# print div42(0)
# print div42(1)
#
#
# print 'howdy dodi, many cats?'
# numcato = raw_input()
# try:
#     if int(numcato) >= 4:
#         print 'got lots of catos'
#     elif int(numcato) < 0:
#         print 'please type a positive number'
# except ValueError:
#     print 'please type a number'

# doesn't work...
# raise ValueError('type positive number')
# except ValueError as vod:
# print vod
# elif int(numcato) < 4:
#     print 'got not that many catos'



# lesson 12: creating a programm...

# guess the number game
# import random
# print 'hello, name please'
# name = raw_input()
# secnam = random.randint(1, 20)
# print 'well ' +name + ', i am thinking of a number between 1 and 20'
#
# # ask player to guess 6 times
# for guesses in range(1, 5):
#     print 'guess what number '
#     guess = int(raw_input())
#     if guess < secnam:
#         print 'guess too low'
#     elif guess > secnam:
#         print 'guess too high'
#     else:
#         break  # this condition is correct guess
#
# if guess == secnam:
#     print 'bravo, ' + 'guessed number correctly'
#     print 'you took ' + str(guesses) + ' guesses'
# else:
#     print 'wrong, number was ' + str(secnam)



# lesson 13: lists

# spam = [['cat', 'dog', 'fish', 'rat'], [10, 20, 40, 60, 100]]
# print spam[0][2]
# print spam[1][2]
# print spam[-1][-1]
# print spam[1][-2]
# print 'the ' + spam[0][2] + 'is afraid of the ' + str(spam[1][3])
#
# s = 'hello'
# print s
# s = [10, 20, 30]
# s[1] = 'hell'  # replaces 20 with hell
# print 'a: ' + str(s)
#
# s[1:3] = ['cat', 'dog', 'mouse']  # puts these values to index 1 to 3
# print 'b: ' + str(s)
#
# s.append('elephant') # adds value to end of list
# print 'c: ' + str(s[:2])  # slice parts of list
# print 'd: ' + str(s[1:])  # slice parts of list
# del s[2]  # delete smth in a list
# print 'e: ' + str(s)
# del s[2]  # delete smth in a list
# print 'f: ' + str(s)
# print 'f: ' + str(len(s))
# ss = s + [1, 2, 3]  # put lists together, called concatenation
# print 'g: ' + str(ss)
# sss = [1, 2, 3] * 2  # list multiplication
# print 'e: ' + str(sss)
# sd = list('hello')
# print sd
#
# sdk = ['jo', 'ho', 'mo', 'ko']
# print 'ho' in sdk
# print 'lo' in sdk



# lesson 14:
# 3 for loops with lists, multiple assignment and augmented assignment operators

# gg = list(range(0, 21, 2))
# print gg
# # for loops with lists
# supplies = ['pens', 'book', 'desk', 'folder', 'head']
# for i in range(len(supplies)):  # go through index and list and print it
#     print 'index ' + str(i) + ' in supplies is: ' + supplies[i]
#
# # multiple assignment
# cat = ['fat', 'orange', 'loud']
# size, color, disposition = cat
# print size
# print color
# print disposition
#
# size, color, disposition = 'skinny', 'black', 'quiet'
# a = 'aaa'
# b = 'bbb'
# a, b = b, a  # swap stuff
# print a
# print b
#
# # augmented assignment operators
# spa = 2
# print spa
# spa = spa + 1
# spam = 6
# spam += 2  # same as above but shorter
# print spam
# same goes for - * / %



# lesson 15:
# methods, and the list methods:
# index, append, insert, remove, sort



# magic 8 ball
# import random
# messages = ['It is certain',
#             'It is decidedly so',
#             'Yes definitely',
#             'Reply hazy try again',
#             'Ask again later',
#             'Concentrate and ask again',
#             'My reply is no',
#             'Outlook not so good',
#             'Very doubtful']
#
# print(messages[random.randint(0, len(messages) - 1)])
#
# print('Four score and seven ' +
#       'years ago...')


import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)  # makes a copy, using copy, list can be changed and original stays the same...
cheese[1] = 42
print spam
print cheese





this is up to chapter 4 in the book: automate the boring stuff with python!








