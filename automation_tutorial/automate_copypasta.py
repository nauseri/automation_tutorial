

# Project: copypasta

# run program with a command line argument like email or blog
# account password will be copied and i just need to paste it to website, yay

# shortcuts to run Python scripts, see appendix B!
# new field starting with: #! python3 and a description comment
# store account name and password as dictionary, like this:

#! python3


# copypasta = {'greeting': 'hello there how do you do',
#              'opinion': 'i do not believe that to be true',
#              'bye': 'was nice chatting with you, hope to see you soon, good bye'}
#
# import sys, pyperclip  # 1st item in sys.argv is script name,
# # 2nd is first command line argument and her thats the name of the account whose password i want
# if len(sys.argv) < 2:
#     print('Usage: py automate_copypasta.py [thekey] - copy a key')  # message if command line arguments isnt inputed.
#     sys.exit()
#
# thekey = sys.argv[1]   # first command line arg is the account name,
# # so mail, blog or luggage that i input in command line
#
# if thekey in copypasta:
#     pyperclip.copy(copypasta[thekey])  # copies key to clipboard, pyperclip needs to be imported
#     print('a key for ' + thekey + ' copied to clipboard.')
# else:
#     print('There is no key named ' + thekey)


# create a batch file and save the file as copypasta.bat in the C:\Windows folder
# @py.exe C:\Python34\automate_copypasta.py %*
# @pause

# now i can run the program on Windows with WIN-R and typing <account name>


# use command prompt, was missing pyperclip... path and pythonpath environment variables different, should be same
# causes problems, solve with these two links or just do pip install pyperclip for now in terminal...
# https://stackoverflow.com/questions/30378105/python-modules-not-found-over-terminal-but-on-python-shell-linux#30379595
# https://stackoverflow.com/questions/431684/how-do-i-change-directory-cd-in-python

# in command prompt (such as anacondy prompt, which is not the same as python interactive terminal!):
# (import os)
# (os.chdir(C:\Users\nauseri\PycharmProjects\repo))

# had to manually do pip install pyperclip in command prompt...
# cd C:\Users\nauseri\PycharmProjects\repo
# py -3 automate_copypasta.py

# in pyhton interactive terminal, check path
# import sys
# print(sys.path)






# Project: Adding Bullets to Wiki Markup
# 1 Paste text from the clipboard
# 2 Do something to it
# 3 Copy the new text to the clipboard

#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

# import pyperclip
# text = pyperclip.paste()
#
# # Separate lines and add stars.
# lines = text.split('\n')
# for i in range(len(lines)):    # loop through all indexes for "lines" list
#     lines[i] = '* ' + lines[i] # add star to each string in "lines" list
# text = '\n'.join(lines)
# pyperclip.copy(text)

