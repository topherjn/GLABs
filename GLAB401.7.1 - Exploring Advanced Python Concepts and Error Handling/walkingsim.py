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
