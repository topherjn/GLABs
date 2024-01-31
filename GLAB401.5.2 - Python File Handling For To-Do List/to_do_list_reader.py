import os
# start reading comments below function
"""
Create a function to receive user input for adding tasks to the to-do list.
Validate the input to ensure the task description is not empty.
Implement user-friendly messages to provide feedback on successful task additions and error conditions.
Write the to-do list tasks to a text file in append mode ("a").
Allow the user to choose whether to add another task or exit the program.
"""
def add_task(task, contents,filename):
    # don't add nothing tasks
    if len(task) == 0:
        return int(-1)   
    
    # capitalize first letter for consistency
    task = task[0].upper() + task[1:]
    contents += "n" + task + "\n"

    # append task to file
    with open(filename,"w") as fd:
        fd.write(contents)

    return int(0)

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
# will crash on File Not Found
# for this version show message
with open(filename) as fd:
    contents = fd.read() # read all contents into string

print("These are the items currently on your list: ")
# print file contents
print(contents)
task = input("What task to you want to add?" )

if add_task('walk the dog',contents,filename) < 0:
    print("Cannot add an empty task")

print("Current list: ")
with open(filename) as fd:
    contents = fd.read()

print(contents)