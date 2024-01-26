import random as rnd

# create a python list of jokes from the jokes here:
# https://datasciencedojo.com/blog/data-science-jokes/#
jokes = ["There are two kinds of data scientists. 1.) Those who can extrapolate from incomplete data.",
"Data science is 80% preparing data, and 20% complaining about preparing data.",
"There are 10 kinds of people in this world. Those who understand binary and those who don't.", "What's the difference between an introverted data analyst & an extroverted one? Answer: the extrovert stares at YOUR shoes.",
"Why did the chicken cross the road? The answer is trivial and is left as an exercise for the reader.",
"The data science motto: If at first, you don't succeed; call it version 1.0",
"What do you get when you cross a pirate with a data scientist? Answer: Someone who specializes in Rrrr",
'A SQL query walks into a bar, walks up to two tables, and asks, "Can I join you?"',
'Why should you take a data scientist with you into the jungle? Answer: They can take care of Python problems','Old data analysts never die - they just get broken down by age']

# get reponse of desire of user
# assume anything not in this list is a yes
negatives = ['no', 'nah', 'quit', 'stop', 'exit', 'nope', 'n', 'negative',  'nay']

reply = input('Would you like to hear a data analyst joke? ')

# loops continues as long as user wants
while reply.lower() not in negatives:

    # pick a random joke
    # not a lot of jokes so probably repetitive
    joke = rnd.randint(0, rnd.randint(0,len(jokes)))

    # 'tell' the joke
    print(jokes[joke])

    # check with user for desire to continue
    reply = input("Would you like to hear another? ")

# think of a pun for a termination message
print("You're humorless.")

