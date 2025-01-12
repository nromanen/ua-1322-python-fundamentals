"""
Write a program that calculates the area of a rectangle,
triangle and circle (write three functions to calculate the area,
and call them in the main program depending on the user's choice).
"""

from math import pi

# Three functions that calculate the area of a rectangle,
# triangle, and circle.

def rectangle(length, width):
    """This function calculates the area of a rectangle."""
    area_rectangle = length * width
    return area_rectangle


def triangle(base, height):
    """This function calculates the area of a triangle."""
    area_triangle = 0.5 * (base * height)
    return area_triangle


def circle(radius):
    """This function calculates the area of a circle."""
    area_circle = pi * radius ** 2
    return round(area_circle, 2)

# get the user's choice and calculate the area.

question = input("Which shape do you want to calculate the area of? : ")

match question.lower():
    case "rectangle":
        length_answer = float(input("Enter the length: "))
        width_answer = float(input("Enter the width: "))
        print(f"Area of the rectangle is {rectangle(length_answer, width_answer)}")
    case "triangle":
        base_answer = float(input("Enter the base: "))
        height_answer = float(input("Enter the height: "))
        print(f"Area of the triangle is {triangle(base_answer, height_answer)}")
    case "circle":
        radius_answer = float(input("Enter the radius: "))
        print(f"Area of the circle is {circle(radius_answer)}")
    case _:
        print("Invalid input")
