"""Task 1: Iterators and Generators"""

# Define a list of words
word_list = ["apple", "banana", "cherry", "date", "fig"]

# Custom iterator function
def custom_iterator(words):
    # Initialize an index
    index = 0
    
    # Define the __next__ method
    def __next__():
        nonlocal index
        if index < len(words):
            word = words[index]
            index += 1
            return word
        else:
            raise StopIteration
    
    # Return an iterable
    return iter(__next__, None)

# Generator function
def word_generator(words):
    for word in words:
        yield word

# Demonstrate the use of the custom iterator
print("Using Custom Iterator:")
iterator = custom_iterator(word_list)
for word in iterator:
    print(word)

# Demonstrate the use of the generator
print("\nUsing Generator:")
generator = word_generator(word_list)
for word in generator:
    print(word)

"""Task 2: Lambda Functions and Closures"""

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Create a lambda function that squares a number
square = lambda x: x**2

# Implement a closure function that applies the square function to each number
def apply_square(numbers_list):
    squared_numbers = []

    def square_number(number):
        return square(number)

    for num in numbers_list:
        squared_numbers.append(square_number(num))

    return squared_numbers

# Apply the closure function to the list of numbers and print the results
result = apply_square(numbers)
print("Original Numbers:", numbers)
print("Squared Numbers:", result)

"""Task 3: Decorators"""

# Define a function greet() that prints a greeting message
def greet(name):
    message = f"Hello, {name}!"
    return message

# Create a decorator function uppercase_decorator() to convert the message to uppercase
def uppercase_decorator(func):
    def wrapper(name):
        modified_message = func(name).upper()
        print(modified_message)
    return wrapper

# Apply the uppercase_decorator to the greet() function
greet = uppercase_decorator(greet)

# Call greet() to see the modified behavior
greet("Alice")
greet("Bob")

"""Task 4: Error Handling"""

# Define a function divide(a, b) that takes two numbers as input and returns the result of a divided by b.
def divide(a, b):
    return a / b

try:
    # Implement a try-except block to handle potential exceptions when dividing by zero.
    result = divide(10, 0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    # Use the assert statement to verify a condition, e.g., that the result of dividing 10 by 2 is 5.
    assert result == 5, "Assertion Error: Result is not as expected."
finally:
    # Create a function with a try, except, else, and finally block to handle exceptions gracefully,
    # print messages at each stage, and ensure resource cleanup.
    print("Division attempt completed.")

# Raise a custom exception using the raise statement when a condition is met, e.g., if b is negative.
def divide_custom_exception(a, b):
    if b < 0:
        raise ValueError("Custom Exception: Division by a negative number is not allowed.")
    return a / b

try:
    result = divide_custom_exception(10, -2)
except ValueError as e:
    print(e)
else:
    print("Result of division:", result)
finally:
    print("Custom exception handling completed.")