"""
Task1. Create a list that contains elements of integer type, then use
the loop to change the type of these elements to a floating type.
(Hint: use the built-in float () function).
"""

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]      # Create a list of integers
float_list = []                                     # Create a list of floats

for x in list:                              # Use a loop to convert each element to a floating-point number
	float_list.append(float(x))

print(f"integer list: {list}")              # Print the list of integers
print(f"float list: {float_list}")                  # Print the list of floats.
print ()

# Alternatively, we can use range(len(sequence)) for iterating over the list:
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(list)):
	list[i] = float(list[i])

print (list)
