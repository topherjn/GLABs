import math as m

def is_prime(number):

    # base cases
    # a prime has precisely 2 factors: itself and 1
    # 1 has only 1 factor; 2 is the first prime and 
    # only even one, there is no room between 2 and
    # 1 for a whole-number factor other than 1 and 2
    if number <= 1: 
        return False
    if number == 2: 
        return True
    
    # square root because only need to go
    # up one side
    for i in range(2,int(m.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

print("First 100 primes: ")
for i in range(1,101):
    if is_prime(i):
        print(i)
