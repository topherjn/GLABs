# Define a parent class
class Shape:
    def __init__(self, color):
        self.color = color

    def get_area(self):
        pass

# Define a subclass
class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

# Create objects of the classes
shape = Shape("Red")
rectangle = Rectangle(5, 3, "Blue")

# Use objects interchangeably
print(shape.color)  # Output: Red
print(rectangle.color)  # Output: Blue
print(rectangle.get_area())  # Output: 15
