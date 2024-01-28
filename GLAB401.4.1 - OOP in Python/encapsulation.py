# Define a class with access modifiers
class Person:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self.__age = age   # Private attribute

    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Age: {self.__age}")

# Create an object of the class
person = Person("John Doe", 25)

# Access protected attribute
print(person._name)  # Output: John Doe

# Attempt to access private attribute
# print(person.__age)  # This will cause an AttributeError

# Access private attribute using name mangling
print(person._Person__age)  # Output: 25

# Call the method to display information
person.display_info()
