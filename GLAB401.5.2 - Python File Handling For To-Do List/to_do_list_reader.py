import os
"""
Organize your code into functions to enhance readability and maintainability.
Create separate functions for reading, writing, and validating user input for the to-do list.
Ensure that each function has a clear purpose and follows best practices for function design.
"""


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
    task = task+'\n'

    # append task to file
    try:
        with open(filename,"a") as fd:
            fd.write(task)
    except Exception:
        print("Something when wrong during writing!")
        exit()
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
try:
    with open(filename) as fd:
        contents = fd.read() # read all contents into string
except Exception:
    print("Sorry, something went wrong")
    exit()

print("These are the items currently on your list: ")
# print file contents
print(contents)
task = input("What task to you want to add?\n'quit' when done: ")

while task.lower() != 'quit':
    # returns -1 on empty
    if add_task(task,contents,filename) < 0:
        print("Cannot add an empty task")

    # give user chance to see update
    print("Current list: ")
    with open(filename) as fd:
        contents = fd.read()

    print(contents)

    # prompts for next task
    task = input("What task to you want to add?\n'quit' when done: ")