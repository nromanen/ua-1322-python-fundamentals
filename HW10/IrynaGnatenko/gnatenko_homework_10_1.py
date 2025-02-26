"""
Create a polygon class and a rectangle class
that inherits from the polygon class
and finds the area of rectangle.
"""

class Polygon:                                     # pylint: disable=too-few-public-methods
    """ Polygon class """
    def __init__(self, no_of_sides):
        self.no_of_sides = no_of_sides
        self.size = [float(input(f"Enter the size of the side {str(i+1)}: ")) for i in range(self.no_of_sides)]

class Rectangle(Polygon):                          # pylint: disable=too-few-public-methods
    """ Rectangle class """
    def __init__(self):
        super().__init__(2)
    def area(self):
        """ Find the area of the rectangle """
        a, b = self.size
        area = a * b
        print(f"The area of the rectangle is {area}")

rectangle = Rectangle()
rectangle.area()
