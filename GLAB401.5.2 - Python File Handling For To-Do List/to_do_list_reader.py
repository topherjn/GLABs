# Organize your code into functions to enhance readability and maintainability.
# Create separate functions for reading, writing, and validating user input for the to-do list.
# Ensure that each function has a clear purpose and follows best practices for function design.

# Starting fresh while referring to saved versions

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

def write_to_todo_list(filename, content, newfile):
    
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

def validate_user_input(input):

    is_valid = False

    # if user clears all the 
    # input errors return true is
    # valid

    # hurdles?
    # file exists?

    return is_valid

# main is here
# testing

# reading files
filename = 'to_do_list.txt'
#filename = 'x'

# the function does the I/O work
contents = read_todo_list(filename)
if contents is not None:
    print(contents)

# adding tasks
    
contents = 'Sleep\nWork\nEat\Sleep'

num_bytes = write_to_todo_list(filename,contents,True)
if num_bytes < 0:
    print("Something went wrong during writing")
else:
    print(f"{num_bytes} characters written to {filename}")

# etc from user

# consider new lists - mode
