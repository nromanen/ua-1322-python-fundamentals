# Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).
from math import pi


def rectangle():
    length = float(input('Enter the length of the rectangle: '))
    width = float(input('Enter the width of the rectangle: '))
    return length * width


def triangle():
    side = float(input('Enter the side of the triangle: '))
    height = float(input('Enter the height of the triangle: '))
    return side * height / 2


def circle():
    radius = float(input('Enter the radius of the circle: '))
    return round(pi * (radius ** 2), 2)


# The user has to enter one of the letters to calculate the area:
# r - for the rectangle;
# t - for the triangle;
# c - for the circle;
# q - to exit the calculation
area = input('Enter "r", or "t", or "c", or "q" to exit: ')
while area:
    match area:
        case 'r':
            result = f'Area of the rectangle = {rectangle()}'
        case 't':
            result = f'Area of the triangle = {triangle()}'
        case 'c':
            result = f'Area of the circle = {circle()}'
        case 'q':
            break
        case _:
            result = 'Wrong letter! Try again:'
    print(result)
    area = input('Enter "r", or "t", or "c", or "q" to exit: ')
