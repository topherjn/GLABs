import os
"""
Write a Python program that reads and displays the contents of a to-do list stored in a text file.
Use the "with" statement for file handling to ensure proper resource management.
Allow the user to input the filename they want to read for the to-do list.
Display a user-friendly message if the file doesn't exist.
"""
# prompt user 
# save user response in variable
filename = input("What is the name of the file you want to open? ")

# if the user messes up yell at user
try:
    while not os.path.isfile(filename):
        print("Sorry, that file does not exist.  Try again.")
        filename = input("What is the name of the file you want to open? ")
except Exception:
    print("Something went wrong with file I/0")
    exit()

# open a file in the cwd with user's input
# exits on file not found for now
# for this version show message
try:
    with open(filename) as fd:
        contents = fd.read() # read all contents into string
except Exception:
    print("Sorry, something went wrong")
    exit()

print("These are the items currently on your list: ")
# print file contents
print(contents)