
from math import pi

# this serves only as a model.  we learn abstract classes
# ABC whatever later
class Shape:
    def __init__(self) -> None:
        pass

    def calculate_area(self):
        pass

# a circle has a radius as base characteristic
class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        return self.__radius * self.__radius * pi
    
# a rectangle is a length and width  
class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        super().__init__()
        self.__length = length
        self.__width = width
    
    def calculate_area(self):
        return self.__length * self.__width

# a Triangle is a base and height
class Triangle(Shape):
    def __init__(self,base,height) -> None:
        super().__init__()
        self.__base = base
        self.__height = height

    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, value):
        self.__base = value

    def calculate_area(self):
        return 0.5 * self.__base *self.__height

# testing
if __name__ == "__main__":

    shape = Circle(radius=4)
    print(str(shape.calculate_area()))

    shape = Rectangle(length=4,width=5)
    print(str(shape.calculate_area()))
    
    shape = Triangle(base=4,height=5)
    print(str(shape.calculate_area()))

    # testing out properties
    shape.base = 12

    print(shape.base)