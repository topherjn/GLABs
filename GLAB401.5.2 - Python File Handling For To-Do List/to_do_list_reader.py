# Organize your code into functions to enhance readability and maintainability.
# Create separate functions for reading, writing, and validating user input for the to-do list.
# Ensure that each function has a clear purpose and follows best practices for function design.

# Starting fresh while referring to saved versions

# for reading anything
def read_todo_list(filename):
    contents = None

    # open the file name 
    # if you can't open file yell at user
    # and return None (i.e. None == error)
    # else read the contents and return them
    try:
        with open(filename) as fd:
            contents = fd.read()
    except FileNotFoundError:
        return "Filename " + filename +": File Not Found"

    return contents

# for writing anything
def write_to_todo_list(filename, contents, newfile=False):
    
    if newfile:
        mode = 'w'
    else:
        mode = 'a'

    # open the file name
    try:
        with open(filename,mode) as fw:
            fw.write(contents)
    except FileNotFoundError:
        return -1
    return len(contents)


    # if you can't open file yell at user
    # and return error true

    # else write the file and return false 
    # if it completes

    return error

# since  I don't know exactly
# what is wanted, I will just check
# for file exists
def validate_user_input(input):

    # if the file can't be found
    # return false for filename
    # not valid
    try:
        with open(filename) as fd:
            pass
    except FileNotFoundError:
        return False

    return True

def add_task(task,filename):

    # don't add nothing tasks
    if len(task) == 0:
        return int(-1)   
    
    # capitalize first letter for consistency
    # and present file might not have newline
    # at EOF
    task = task[0].upper() + task[1:]
    newtask = task + '\n'

    # append task to file
    # default mode append i.e. newfile false
    if write_to_todo_list(filename, newtask) >= 0:
        print(f"{task} added to list")
    
    return int(0)

# main is here
# testing

# etc from user
filename = input("What is the name of the file you want to open? ")
filename = 'to_do_list.txt' # for testing

while not validate_user_input(filename):
    print(F"File {filename} not found. Try Again:")
    filename = input("What is the name of the file you want to open? ")

# creating a new list
# newfile == true
# let I/O wrapper functions do the work   
contents = "Sleep\nWork\nEat\nSleep\n"

num_bytes = write_to_todo_list(filename,contents,True)
if num_bytes < 0:
    print("Something went wrong during writing")
else:
    print(f"{num_bytes} characters written to {filename}")

    # the function does the I/O work
contents = read_todo_list(filename)
if contents is not None:
    print(contents)

# adding tasks
task = input("What task to you want to add?\n'quit' when done: ")

while task.lower() != 'quit':
    # returns -1 on empty
    if add_task(task,filename) < 0:
        print("Cannot add an empty task")

    # give user chance to see update
    print("Current list: ")
    print(read_todo_list(filename))

    # prompts for next task
    task = input("What task to you want to add?\n'quit' when done: ")