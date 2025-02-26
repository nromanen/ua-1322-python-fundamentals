"""
Create a polygon class and a rectangle class
that inherits from the polygon class and finds the square
of rectangle.
"""

class Polygon:
    """This is a base class."""

    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2


class Rectangle(Polygon):
    """This is a child class of Polygon."""

    def square_rectangle(self):
        return self.side_1 * self.side_2


rectangle_1 = Rectangle(3, 2)

print(rectangle_1.square_rectangle())
