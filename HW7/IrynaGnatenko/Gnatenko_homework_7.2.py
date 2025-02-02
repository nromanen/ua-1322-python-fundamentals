"""
Task2. Write a program that calculates the area of a rectangle,
triangle and circle (write three functions to calculate the area,
and call them in the main program depending on the user's choice).

rectangle area = width * length
triangle area = base * height / 2
circle area = π * radius * radius
"""

PI = 3.1415926535

def area_rectangle(width, length):
	"""calculates area of a rectangle"""
	return width * length

def area_triangle(base,height):
	"""calculates area of a triangle"""
	return base * height / 2

def area_circle(radius):
	"""calculates area of a circle"""
	return PI * radius ** 2

def calculate_area (shape):
	"""accepts a shape and its dimensions as an input and returns an area of the given shape"""
	match shape:
		case "rectangle":
			width = float(input("what is the width? "))
			length = float(input("what is the length? "))
			area = area_rectangle(width, length)
		case "circle":
			radius = float(input("what is the radius? "))
			area = area_circle(radius)
		case "triangle":
			base = float(input("what is the base? "))
			height = float(input("what is the height? "))
			area = area_triangle(base,height)
		case _:
			print ("sorry, I don't know how to calculate the area of this shape")
			return
	print("the area is:", area)

shape = input("What shape is it? Triangle, circle or rectangle? ")
calculate_area(shape)