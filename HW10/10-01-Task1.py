class Polygon():
    '''General polygon class'''
    def __init__(self, sides):
        self.sides = [0 for x in range(sides)]

class Rectanle(Polygon):
    '''Specific class for rectangles'''
    def __init__(self):
        super().__init__(2)
    
    def square(self):
        if any(self.sides):
            return self.sides[0]*self.sides[1]
        else:
            return "Please use configSides() function to configure the sides!"
    
    def configSides(self):
        self.sides = [float(input(f"Enter Side {x + 1}/{len(self.sides)}: " )) for x in range(len(self.sides))]



if __name__ == "__main__":
    t = Rectanle()
    t.configSides()
    print(t.square())