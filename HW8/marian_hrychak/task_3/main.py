from math_utils import *

question = input("Which figure do you want to calculate the area of? : ")

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
