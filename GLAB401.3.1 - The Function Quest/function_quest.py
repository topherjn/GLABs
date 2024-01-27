# The Mighty Calculator
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

result = add_numbers(5, 3)
print("The sum is:", result)

result = subtract_numbers(10, 4)
print("The difference is:", result)

result = multiply_numbers(6, 2)
print("The product is:", result)

result = divide_numbers(15, 0)
print("The quotient is:", result)
