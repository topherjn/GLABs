"""
Write a Python program that reads and displays the contents of a to-do list stored in a text file.
Use the "with" statement for file handling to ensure proper resource management.
Allow the user to input the filename they want to read for the to-do list.
Display a user-friendly message if the file doesn't exist.
"""
# note: I am saving error checking for future tasks

# make sure it's the current directory for this project on my machine
path = "D:\\Per Scholas\\GLABs\\GLAB401.5.2 - Python File Handling For To-Do List\\"

# prompt user 
# save user response in variable
filename = input("What is the name of the file you want to open? ")

# open a file in the cwd with user's input
# will crask on File Not Found
with open(filename) as fd:
    contents = fd.read() # read all contents into string

# print file contents
print(contents)



