

# automate chp 6: Manipulating Strings


# Escape character
# Prints as
# \' Single quote
# \" Double quote
# \t Tab
# \n Newline (line break)
# \\ Backslash

# print("Hello there!\nHow are you?\nI\'m doing fine.")
# print(r'That is catmandu\'s cat.')  # r prints everything
# print('''Dear Alice,
#
# Eve's cat has been arrested for catnapping, cat burglary, and extortion.
#
# Sincerely,
# Bob''')  # multiple lines
#
# # Multiline Comments
# """This is a test Python program.
# This program was designed for Python 3, not Python 2.
# """
# def spam():
#     """This is a multiline comment to help
#     explain what the spam() function does."""
#     print('Hello!')
#
# # Indexing and Slicing Strings
# # in and not in Operators with Strings
# print 'Hello' in 'Hello World'
# print 'HELLO' in 'Hello World'
# print '' in 'spam'
# print 'cats' not in 'cats and dogs'

# The upper(), lower(), isupper(), and islower() String Methods

# The isX String Methods
# is...()  returns a Boolean value
# isalpha() returns True if the string consists only of letters and is not blank.
# isalnum() returns True if the string consists only of letters and numbers and is not blank.
# isdecimal() returns True if the string consists only of numeric characters and is not blank.
# isspace() returns True if the string consists only of spaces, tabs, and new-lines and is not blank.
# istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

# The startswith() and endswith() String Methods, are alternatives to the == equals operator

# The join() and split() String Methods, for a list of strings that need to be joined
# Justifying Text with rjust(), ljust(), and center()
# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 14, 7)
# printPicnic(picnicItems, 20, 6)

# Removing Whitespace with strip(), rstrip(), and lstrip()


# Copying and Pasting Strings with the pyperclip Module
# The pyperclip module has copy() and paste() functions that can
# send text to and receive text from your computers clipboard
# pip install pyperclip

# import pyperclip
# pyperclip.copy('Hello world!')
# print pyperclip.paste()



# Project: Password Locker: password manager program

# run program with a command line argument like email or blog
# account password will be copied and i just need to paste it to website, yay

# shortcuts to run Python scripts, see appendix B!
# new fiel starting with: #! python3 and a description comment
# store account name and password as dictionary, like this:

#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip  # 1st item in sys.argv is script name,
# 2nd is first command line argument and her thats the name of the account whose password i want
if len(sys.argv) < 2:
    print('Usage: py py.py [account] - copy account password')  # message if command line arguments isnt inputed.
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name,
# so mail, blog or luggage that i input in command line

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])  # copies key to clipboard, pyperclip needs to be imported
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)










