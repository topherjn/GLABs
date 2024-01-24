"""The Battle of Lists: Write a program that compares two lists and finds the common elements between them. Display the matching items and the total count of matches
"""
import random as rand

# custom random ints function
def create_random_list():
    number_list = []

    for i in range(0, 20):
        number_list.append(rand.randint(1,100))
    return number_list

# create two lists
list1 = create_random_list()
list2 = create_random_list()
common = []

print(list1)
print(list2)
# iterate over one and look for items in other
# add duplicates to a new list
for item in list1:
    if item in list2:
        common.append(item)


# repeat in other direction, perhaps skipping items already known?
for item in list2:
    if item in list1:
        common.append(item)

# turn common list into set to get rid of dupes
# print set of common elements
# print length of third list
common = set(common)
print("Common elements: ")
print(common)
print("Number in common: " + str(len(common)))