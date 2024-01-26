"""
The Quest for Sorting: Create a program that takes a list of numbers 
and sorts them in ascending or descending order. Challenge yourself 
to implement sorting algorithms like bubble sort or insertion sort.
"""

# custom random ints function
def create_random_list():
    number_list = []

    for i in range(0, 20):
        number_list.append(rand.randint(1,100))
    return number_list

# create list of numbers.  random?
import random as rand

number_list = create_random_list()

# use built-in sorting
print(f"Original pseudorandom list of integers: {number_list}")
# sort list with built-in
number_list.sort()
print(f"Built-in sorted ascending: {number_list}")
number_list.sort(reverse=True)
print(f"Built-in sorted descending: {number_list}")

# bubble sort
# note - no tweaks for efficiency
def bubble_sort_list(list_to_sort):

    num_items = len(list_to_sort)

    for i in range(num_items):
        for j in range(num_items):

            if(list_to_sort[i] < list_to_sort[j]):
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[j]
                list_to_sort[j] = temp

def insertion_sort_list(list_to_sort):

    num_items = len(list_to_sort)

    for i in range(1,num_items):
        # place each item one at a time
        item_to_place = list_to_sort[i]

        # get index of item in front of i
        j = i - 1

        # while the item to place is in the wrong
        # order, push everything back
        while j >= 0 and item_to_place < list_to_sort[j]:
            list_to_sort[j+1] = list_to_sort[j]
            j -= 1
        # once everything is smaller than item
        # drop it in
        list_to_sort[j+1] = item_to_place

# test bubble
number_list = create_random_list()

print(f"Original pseudorandom list of integers: {number_list}")

bubble_sort_list(number_list)

print(f"After bubble sort: {number_list}")

# test insertion sort
number_list = create_random_list()

print(f"Original pseudorandom list of integers: {number_list}")

insertion_sort_list(number_list)

print(f"After insertion sort: {number_list}")

