


# Chapter 5  Dictionaries and Structuring Data
# Indexes for dictionaries are called keys and each key has a value


# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# print myCat['size']
# print 'My cat has ' + myCat['color'] + ' fur.'
#
# spam = {12345: 'Luggage Combination', 42: 'The Answer'}


# Dictionaries vs. Lists: dic are unordered
# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# while True:
#     print('Enter a name: (blank to quit)')
#     name = raw_input()
#     if name == '':
#         break
#
#     if name in birthdays:
#              print(birthdays[name] + ' is the birthday of ' + name)
#
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = raw_input()
#         birthdays[name] = bday
#         print('Birthday database updated.')


# spam = {'color': 'red', 'age': 42}
# for k, v in spam.items():
#     print(k + ': ' + str(v))
# # spam.keys():
# # spam.values():



# get() method to retrieve values, returns 0 if it doesnt exist
# setdefault() Method
# pprint module

# A Tic-Tac-Toe Board
# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# printBoard(theBoard)
#
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = raw_input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'
# printBoard(theBoard)


# Nested Dictionaries and Lists
# Lists are useful to contain an ordered series of values, and
# dictionaries are useful for associating keys with values.
# dic within a dic
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought
print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))




























