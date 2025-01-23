from math import pi, pow

def rectangle_area(width, height):
    """Calculates rectangle area"""
    return width * height

def triangle_area(base, height):
    """Calculates triangle area"""
    return 0.5 * base * height

def circle_area(radius):
    """Calculates circle area"""
    return (pi * pow(radius, 2))