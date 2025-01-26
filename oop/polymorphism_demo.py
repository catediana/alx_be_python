#creating a shape class
import math

class Shape:
    def area(self):
        """Raise NotImplementedError to indicate that this method should be overridden."""
        raise NotImplementedError("Derived classes need to override the area() method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the rectangle's area."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Override the area method to calculate the circle's area."""
        return math.pi * self.radius ** 2

