"""
Task1. Write a function that returns the largest number of two
numbers (use DocStrings documentation strings in the function).
"""

def bigger_number (num1, num2):
	""" this function takes a pair of integers and returns the bigger one """
	if num1>num2:
		result = num1
	elif num2>num1:
		result = num2
	elif num1 == num2:
		result = "the numbers are equal"
	return result

print(bigger_number(-90,-800)) # printing a result of an example function call