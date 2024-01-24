import random as rand

# create two lists
def create_random_list():
    number_list = []

    for i in range(0, 20):
        number_list.append(rand.randint(1,100))
    return number_list

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

# print length of third list
print("Common elements: ")
print(common)
print(len(common))