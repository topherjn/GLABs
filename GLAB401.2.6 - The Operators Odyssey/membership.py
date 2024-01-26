import random as rnd 

die1 = rnd.randint(0,6) + 1
die2 = rnd.randint(0,6) + 1

if die1+die2 in [7,11]:
    print("You win!")