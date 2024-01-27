# the following function will return the nth fibonacci number
# in the sequence.  I include 0, 1, 1 as 1st, 2nd, 3rd

def fibonacci(nth):
    # base cases
    if nth == 1:
        return 0
    if nth in (2,3):
        return 1
    
    # recursive part
    return fibonacci(nth-1) + fibonacci(nth-2)

# print the 19th fibonacci number by MY
# number scheme, which no one does on the 
# internet.  the 19th was the first one
# I noticed the discrepancy
print(fibonacci(19))

# print the first few to be sure
# starting with 1st, not 0th
for i in range(1, 21):
    print(fibonacci(i))