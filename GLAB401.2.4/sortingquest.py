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

# insertion sort

