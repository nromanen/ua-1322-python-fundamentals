"""
Task1. Create a list that contains elements of integer type, then use
the loop to change the type of these elements to a floating type.
(Hint: use the built-in float () function).
"""

integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]      # Create a list of integers
float_list = []                                     # Create a list of floats

for x in integer_list:                              # Use a loop to convert each element to a floating-point number
	float_list.append(float(x))

print(f"integer list: {integer_list}")              # Print the list of integers
print(f"float list: {float_list}")                  # Print the list of floats.