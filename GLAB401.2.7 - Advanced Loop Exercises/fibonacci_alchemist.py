"""
The Fibonacci Sequence pops up a lot in natural growth processes.
Start with 0 and 1, add them together, and the added that sum
to the previous sum iteratively.  The beginning of the Sequence,
which is countably infinite:
0, 1, 1, 2, 3, 5, 8, 13, 21, ...

The loop in this program will return the nth Fibo number in the sequence
"""

def fibonacci(nth):

    # in recursive these would be based cases:
    if nth == 1: 
       return 0
    if nth in [2,3]:
        return 1
    

    fibo1 = 1
    fibo2 = 1
    sum = 0

    # with base cases out of the way do the
    # rest.  Each iteration
    # we save the sum of two numbers and add that
    # number to the next iteration number.
    # N.B. this is not cumulative like factorial
    for i in range(3, nth):
        sum = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = sum

    # the sum should hold the nth
    # fibo number
    return sum

# test by generating the first so-many fibos
# start counting with 0 as the first
for i in range(1,20):
    print(f"The {i}th Fibonacci number is: {fibonacci(i)}")