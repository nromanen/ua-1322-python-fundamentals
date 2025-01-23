# Create a polygon class and a rectangle class
# that inherits from the polygon class and finds the square
# of rectangle.


class Polygon:
    def __init__(self, sides, size):
        self.sides = sides
        self.size = size

    def size_side(self):
        self.size = [float(input(f'Enter the side {str(i + 1)}: ')) for i in range(self.sides)]


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2, 0)

    def area(self):
        a, b = self.size
        area = a * b
        print(area)


r = Rectangle()
r.size_side()
r.area()
