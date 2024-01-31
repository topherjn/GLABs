"""
Write a Python program that reads and displays the contents of a to-do list stored in a text file.
Use the "with" statement for file handling to ensure proper resource management.
Allow the user to input the filename they want to read for the to-do list.
Display a user-friendly message if the file doesn't exist.
"""
import os
# prompt user 
# save user response in variable
filename = input("What is the name of the file you want to open? ")

# if the user messes up yell at user
while not os.path.isfile(filename):
    print("Sorry, that file does not exist.  Try again.")
    filename = input("What is the name of the file you want to open? ")

# open a file in the cwd with user's input
# will crask on File Not Found
with open(filename) as fd:
    contents = fd.read() # read all contents into string

# print file contents
print(contents)



