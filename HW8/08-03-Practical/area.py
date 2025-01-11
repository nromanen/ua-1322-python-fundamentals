import math

def rect_area(heigh: float, base: float) -> float:
    return heigh*base

def triangle_area(height: float, base: float) -> float:
    return 0.5*height*base

def circle_area(radius: float) -> float:
    return math.pi*pow(radius, 2)