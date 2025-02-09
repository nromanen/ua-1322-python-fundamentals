import math

def rectangle(length, width):
    """This function calculates the area of a rectangle."""
    return length * width


def triangle(h, a):
    """This function calculates the area of a triangle."""
    return 0.5 * h * a


def circle(radius):
    """This function calculates the area of a circle."""
    return round(math.pi * math.pow(radius, 2), 2)
