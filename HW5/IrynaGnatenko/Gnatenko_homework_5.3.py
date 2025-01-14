"""
Write a script that will calculate the factorial of the entered
number without using recursion.
Example: 0!=1, 1!=1, 2!=1*2, 3!= 1*2*3=6, ….
"""

input_number = int(input("Please enter the number "))
factorial = 1
range_start = 1
range_end = input_number + 1

for i in range (range_start, range_end):
	factorial *= i

print(f"Factorial of {input_number} is {factorial}")