class Polygon:
    def __init__(self, sides):
        self.sides = sides  

    def perimeter(self):
        return sum(self.sides)  

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height, width, height])

    def area(self):
        width, height = self.sides[0], self.sides[1]
        return width * height 

rect = Rectangle(5, 3)

print(f"Площа прямокутника: {rect.area()}")
print(f"Периметр прямокутника: {rect.perimeter()}")
