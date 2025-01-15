"""
A four-digit natural number is specified:
- find the product of the digits of this number
- write the number in reverse order
- in ascending order, you need to sort the numbers included in the given number
"""

#ask user for an input
number_string = input("Please input a four-digit natural number: ")
error_message = "This doesn't seem to be a four-digit natural number"

#check if the input is a four-digit natural number
try:
	number_integer = int(number_string)
	if number_integer >= 1000 and number_integer <= 9999:
		print(f"Awesome, {number_integer} is a four-digit natural number")
	else:
		print (f"{error_message}")
except ValueError:
	print (f"{error_message}")

#find the product of the digits of this number
if 'number_integer' in vars() and number_integer >= 1000 and number_integer <= 9999:
	digits = []
	number_integer_temp1 = number_integer			# create a temporary variable for conversion to list

	while number_integer_temp1 > 0:
		digits.append(number_integer_temp1 % 10)	# get the last digit
		number_integer_temp1 //= 10				# remove the last digit
	digits.reverse()							# reverse the list to restore original order

	current_digit = int(digits[0])
	product = 1

	for current_digit in digits:
		product *= current_digit

	print(f"The product of digits {digits} is {product}")

# write the number in reverse order
if 'number_integer' in vars() and number_integer >= 1000 and number_integer <= 9999:
	reverse_digits = list(reversed(digits))
	print(f"{number_integer} in reverse is {reverse_digits}")

# in ascending order, you need to sort the numbers included in the given number
if 'number_integer' in vars() and number_integer >= 1000 and number_integer <= 9999:
	digits_sorted_asc = list(sorted(digits))
	print(f"{number_integer} sorted in ascending order is {digits_sorted_asc}")

