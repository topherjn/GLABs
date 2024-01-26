import random as rnd

treasure = rnd.randint(0,101)
treasure = 65

guess = 0

# ask use for whole number in regular numerals
# if they type something silly yell at user
# this is a primer for the loop
try:
    guess = int(input('What number do you think hides the treasure (1 - 100)? '))
except ValueError:
    print("Please enter a whole number in Hindu numerals. ")

# as long as the user is wrong let them know how close they are
while guess != treasure:
    if abs(treasure - guess) < 5:
        print("You're red hot!")
    elif abs(treasure - guess) < 10:
        print("You're getting warmer!")
    else:
        print("Ice cold!")
\
    # set up the next guess
    try:
        guess = int(input('What number do you think hides the treasure (1 - 100)? '))
    except ValueError:
        print("Please enter a whole number in Hindu numerals. ")



# loop ends when they guess the answer
print("You found the treasure! ")