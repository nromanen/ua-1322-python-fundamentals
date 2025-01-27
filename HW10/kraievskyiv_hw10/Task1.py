class Polygon():
    """
    A class to represent a generic polygon.
    """
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        """
        Prompts the user to input the lengths of the sides of the polygon.
        """
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range(self.n)]

    def display_sides(self):
        """
        Displays the lengths of all the sides of the polygon.
        """
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")


class Rectangle(Polygon):
    """
    A class to represent a rectangle, inherited from the Polygon class.
    """
    def __init__(self):
        super().__init__(2)

    def find_square(self):
        """
        Calculates and prints the area (square) of the rectangle.
        """
        a, b = self.sides
        print(f"Square of rectangle is {a * b}")\
        

obj = Rectangle()

obj.input_sides()
obj.display_sides()
obj.find_square()  