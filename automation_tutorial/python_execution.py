# https://automatetheboringstuff.com/appendixb/

# ::convenient ways to execute Python scripts::
# shebang line, tells computer to execute program
#
# On Windows, the shebang line is #! python3.
# On Linux, the shebang line is #! /usr/bin/python3.

#! python3.

# You will be able to run Python scripts from an IDE without
# the shebang line, but line is needed to run from command line.

# type this in terminal
# C:\Users\ILKI>cd  C:\Users\ILKI\Documents\repo0
# C:\Users\ILKI\Documents\repo0>py -3 python_execution.py

# make .bat batch file for convenience, runs it with py.exe
# make a new text file containing a single line like the following:

# @py.exe C:\Users\ILKI\Documents\repo0\python_execution.py %*

# save this file with a .bat file extension:
# python_execution.bat
# with this, no need to type full path to run it, place all
# batch files in a single location

# in search, edit path in system variables and add folder path for the pythonscript
# now, with WIN-R and enter script name, i can run the script, non need to type in full path...























