# Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).
from math import pi


def rectangle(a, b):
    area_rectangle = a * b
    return area_rectangle


def triangle(s, h):
    area_triangle = s * h / 2
    return area_triangle


def circle(r):
    area_circle = round(pi * (r ** 2), 2)
    return area_circle


# The user has to enter one of the letters to calculate the area:
# r - for the rectangle;
# t - for the triangle;
# c - for the circle
area = input('Enter "r", or "t", or "c": ')
if area == 'r':
    length = float(input('Enter the length of the rectangle: '))
    width = float(input('Enter the width of the rectangle: '))
    result = f'Area of the rectangle = {rectangle(length, width)}'
elif area == 't':
    side = float(input('Enter the side of the triangle: '))
    height = float(input('Enter the height of the triangle: '))
    result = f'Area of the triangle = {triangle(side, height)}'
elif area == 'c':
    radius = float(input('Enter the radius of the circle: '))
    result = f'Area of the circle = {circle(radius)}'
else:
    result = "Wrong letter! Can't calculate!"
print(result)
