# Define a class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

# Create objects of the class
rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(4, 6)

# Access attributes and call methods
print(rectangle1.width)  # Output: 5
print(rectangle2.get_area())  # Output: 24