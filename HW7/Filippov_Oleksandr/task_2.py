#Task2. Write a program that calculates the area of a rectangle, triangle and circle (write three functions to calculate the area.
#And call them in the main program depending on the user's choice).

import math

def area_rectangle(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle

    Returns:
    float: The area of the rectangle
    """
    return length * width

def area_triangle(base, height):
    """
    Calculate the area of a triangle.

    Parameters:
    base (float): The base of the triangle
    height (float): The height of the triangle

    Returns:
    float: The area of the triangle
    """
    return 0.5 * base * height

def area_circle(radius):
    """
    Calculate the area of a circle.

    Parameters:
    radius (float): The radius of the circle

    Returns:
    float: The area of the circle
    """
    return math.pi * radius ** 2


def main():
    print("Choose the shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {area_rectangle(length, width):.2f}")
    elif choice == 2:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: {area_triangle(base, height):.2f}")
    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {area_circle(radius):.2f}")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()