class Polygon:
    pass


class Rectangle(Polygon):
    def __init__(self, height, length):
        self.height = height
        self.length = length
        self.square = self.calculate_square()
        self.get_square()

    def calculate_square(self):
        return self.height * self.length

    def get_square(self):
        print(f"The square of the rectangle is: {self.square}")


while True:
    height = input("Enter the height of the rectangle: ")
    length = input("Enter the length of the rectangle: ")

    if height.isnumeric() and length.isnumeric():
        height = float(height)
        length = float(length)
        rectangle = Rectangle(height, length)
        break
    else:
        print("Please enter valid numeric values for height and length!")

        # Or like in example in lesson


class Polygon:
    def __init__(self, no_side):
        self.n = no_side
        self.side = [0 for i in range(no_side)]

    def new_side(self):
        self.side = [float(input(f"Enter side {i+1}: ")) for i in range(self.n)]

    def output_side(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.side[i]}")


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def calculate_square(self):
        # Перевіряємо, чи достатньо сторін для розрахунку площі
        if len(self.side) >= 2:
            a, b = self.side[0], self.side[1]
            s = a * b
            print(f"The square of the rectangle is: {s}")
        else:
            print("Not enough sides to calculate the square.")
