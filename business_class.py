# Your Task
# Create a base class named Shape with a method called area that returns 0 by default.

# Then, define three subclasses: Circle, Square, and Triangle.

# Each subclass should override the area method to calculate and return the area of the shape (use π = 3.14 for the circle).

# Next step
# Create a function called print_area that takes a Shape object and prints its area.

# Use this function to print the area of instances of Circle, Square, and Triangle.

# Example Usage
# Your classes should be usable as follows:

# circle = Circle(radius=5)
# print(circle.area())  # Expected output: 78.5 (π * radius^2)

# square = Square(side=4)
# print(square.area())  # Expected output: 16 (side^2)

# triangle = Triangle(base=6, height=4)
# print(triangle.area())  # Expected output: 12 (0.5 * base * height)

# # Demonstrate your function
# print_area(circle)  # Expected to print: 78.5
# print_area(square)  # Expected to print: 16
# print_area(triangle)  # Expected to print: 12
# Guidelines
# Implement the Shape class as a base class with an area method that returns 0.
# The Circle class should have an __init__ method that initializes a radius attribute and overrides the area method to calculate the area of a circle.
# The Square class should have an __init__ method that initializes a side attribute and overrides the area method to calculate the area of a square.
# The Triangle class should have an __init__ method that initializes base and height attributes and overrides the area method to calculate the area of a triangle.
# Demonstrate polymorphism by creating a function that takes a Shape object and prints its area, then call this function with instances of Circle, Square, and Triangle.
# Remember to use proper class inheritance syntax and method overriding to accomplish the task.

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 1/2 * self.base * self.height

circle = Circle(radius=5)
print(circle.area())

square = Square(side=4)
print(square.area())

triangle = Triangle(base=6, height=4)
print(triangle.area())

