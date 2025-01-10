# Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).
from math import pi


def rectangle():
    length = float(input('Enter the length of the rectangle: '))
    width = float(input('Enter the width of the rectangle: '))
    area_rectangle = length * width
    return area_rectangle


def triangle():
    side = float(input('Enter the side of the triangle: '))
    height = float(input('Enter the height of the triangle: '))
    area_triangle = side * height / 2
    return area_triangle


def circle():
    radius = float(input('Enter the radius of the circle: '))
    area_circle = round(pi * (radius ** 2), 2)
    return area_circle


# The user has to enter one of the letters to calculate the area:
# r - for the rectangle;
# t - for the triangle;
# c - for the circle
area = input('Enter "r", or "t", or "c": ')
while area not in ['r', 't', 'c']:
    area = input('Wrong letter! Try again: ')
match area:
    case 'r':
        print(f'Area of the rectangle = {rectangle()}')
    case 't':
        print(f'Area of the triangle = {triangle()}')
    case 'c':
        print(f'Area of the circle = {circle()}')
