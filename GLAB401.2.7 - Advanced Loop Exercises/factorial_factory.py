"""
factorial n! of a number is defined as:
n! = n * n - 1 * n * 2 * ... * 1
but this is also
n * (n-1)! and so on, thus recursive

but loops are faster when not always easier
"""

def factorial(number):
    product = 1

    for i in range(1, number + 1):
        product = product * i
    
    return product

number = int(input('Please enter a number for which you want its factorial: '))

while number < 0: 
    int(input('Please enter a positive integer: '))
    number = int(input('Please enter a number for which you want its factorial: ')) 

result = factorial(number)

print(f'The factorial of {number} is {result}')