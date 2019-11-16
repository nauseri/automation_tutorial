

# road to automation



# lesson 1 and 2

# troubleshoot
# explain what i am trying to do, not just what i did

# for an error message, specify the point at which the error happens

# copy and paste the entire error message and your code to a pastebin site
# like pastebin.com or gist.github.com

# explain what i have already tried to do to solve the problem

# list the version of python that i am using



# lesson 3

# print 'whatsup, you are?'
# myname = raw_input()
# print 'hello ' + myname
# print 'namelength is ' + str(len(myname))
# print 'age is?'
# myage = raw_input()
# print 'you will be ' + str(int(myage) + 1) + ' in a year.'



# lesson 4
# boolean only True or False, can store it in a variable
# True and False always with a big letter first and then small ones
# go = True
# print go

# comparison operators: == , != , < , > , <= , >=
# print 2 != 1
# print 4 == 1
# boolean operators: and , or , not
# print True and True
# l = True
# d = False
# print 'sigi'
# print l and d == True
# print l or d == False
# print not d



# lesson 5
# flow control statements like if and else

# print 'state your name '
# you = raw_input()
# if 'alice' == you:
#     print 'hello there ' + you
# elif you == 'bob':
#     print 'hello there ' + you
# else:
#     print "can't enter here"



# lesson 6
# while loop
# spam = 0
# while spam < 3:
#     print 'hello there'
#     spam = spam + 1

# name = ''
# while name != 'anon':
#     print('type in your name')
#     name = raw_input()
# print 'finally'

name = ''
while True:
    print('type in your name')
    name = raw_input()
    if name == 'anon':
        break  # here, the while statement is terminated 
print 'finally'


spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue  # here, it jumps back to the while loop and no print happens
    print 'spam is ' + str(spam)

















