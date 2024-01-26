import random as rnd

treasure = rnd.randint(0,101)
treasure = 65

guess = 0

try:
    guess = int(input('What number do you think hides the treasure (1 - 100)? '))
except ValueError:
    print("Please enter a whole number in Hindu numerals. ")

while guess != treasure:
    if abs(treasure - guess) < 5:
        print("You're red hot!")
    elif abs(treasure - guess) < 10:
        print("You're getting warmer!")
    else:
        print("Ice cold!")

    try:
        guess = int(input('What number do you think hides the treasure (1 - 100)? '))
    except ValueError:
        print("Please enter a whole number in Hindu numerals. ")




print("You found the treasure! ")