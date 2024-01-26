# The Word Alchemist
"""
The Word Alchemist: Create a program that counts the number of occurrences of each word in a given text.
Use string manipulation techniques to split the text into words and update a dictionary with the word counts.
"""

# get phrase from user 
text = input("Enter a phrase: ")

# create a list from the individual words
words = text.split()

# create an empty dictionary to store counts of those words
occurrences = {}


for word in words:
# check in dictionary for word already there
    # if not there add to dictionary and set value to one
    if not word in occurrences:
        occurrences[word.lower()] = 1
    # if there get current value and increment by one
    else:
        occurrences[word.lower()] += 1

# print out whole dictionary
for word in occurrences:
    print(word, occurrences[word])

# share with the class


