"""
The Quest for Sorting: Create a program that takes a list of numbers 
and sorts them in ascending or descending order. Challenge yourself 
to implement sorting algorithms like bubble sort or insertion sort.
"""

# create list of numbers.  random?
import random as rand

number_list = []

for i in range(0, 20):
    number_list.append(rand.randint(1,100))


# use built-in sorting
print(f"Original pseudorandom list of integers: {number_list}")
# sort list with built-in
number_list.sort()
print(f"Built-in sorted ascending: {number_list}")
number_list.sort(reverse=True)
print(f"Built-in sorted descending: {number_list}")

# bubble sort

# create a swap list items function for both kinds of sorts
# note - no tweaks for efficiency
def bubble_sort_list(list_to_sort):

    num_items = len(list_to_sort)

    for i in range(num_items):
        for j in range(num_items):

            if(list_to_sort[i] < list_to_sort[j]):
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[j]
                list_to_sort[j] = temp

# test bubble
number_list = []
for i in range(0, 20):
    number_list.append(rand.randint(1,100))

print(f"Original pseudorandom list of integers: {number_list}")

bubble_sort_list(number_list)

print(f"After bubble_sort: {number_list}")

# insertion sort
number_list = []
for i in range(0, 20):
    number_list.append(rand.randint(1,100))
    
print(f"Original pseudorandom list of integers: {number_list}")