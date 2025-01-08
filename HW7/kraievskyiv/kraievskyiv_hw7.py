#Task 1
def largest_of_two():
    """This function takes
    two numbers and returns 
    the largest one."""
    while True:  
        a = input("Enter the first number: ")
        b = input("Enter the second number: ")
        #Check if the input is a number
        if a.isnumeric() and b.isnumeric():
            #Convert the input to integer
            a, b = int(a), int(b)
            if a > b:
                return f"The largest number is {a}"
            elif b > a:
                return f"The largest number is {b}"
            return "The numbers are equal"
        print("Invalid input. Please enter valid numbers.")

#Print the function's docstring
print(largest_of_two.__doc__)
#Call the function and print the result
print(largest_of_two())


#Task 2
"""I wanted to try match case for once. 
Don't know if it's correct usage of it,
but everything works."""
#Import pi for circle area
from math import pi

#Define functions to calculate each figure's area
def rectangle_area(width, height):
    """Calculates rectangle area"""
    return width * height

def triangle_area(base, height):
    """Calculates triangle area"""
    return 0.5 * base * height

def circle_area(radius):
    """Calculates circle area"""
    return (pi * radius ** 2)

while True:
    #Ask user to choose the figure
    figure = input("Enter the figure (rectangle, triangle or circle): ").lower()
    #Depending on the figure, ask for the necessary parameters
    #and call the corresponding function to print the area
    match figure:
        case "rectangle":
            width = float(input("Enter the width: "))
            height = float(input("Enter the height: "))
            print(f"The area of the rectangle is {rectangle_area(width, height)}")
            break
        case "triangle":
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            print(f"The area of the triangle is {triangle_area(base, height)}")
            break
        case "circle":
            radius = float(input("Enter the radius: "))
            print(f"The area of the circle is {circle_area(radius)}")
            break
        case _:
            print("Invalid figure. Enter rectangle, triangle or circle.")


#Task 3
def char_number():
    """This function takes a string and returns the number of it's characters."""
    string = input("Enter the string: ").lower()
    #Create an empty list to store the characters and their counts
    lst = []
    for i in string:
        lst.append((i, string.count(i)))
    #Turn the list into a dictionary
    lst = dict(lst)
    return lst

#Call the function and print the result
print(char_number())