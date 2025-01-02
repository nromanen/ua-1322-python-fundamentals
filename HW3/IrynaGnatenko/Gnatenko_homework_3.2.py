"""
A four-digit natural number is specified:
- find the product of the digits of this number
- write the number in reverse order
- in ascending order, you need to sort the numbers included in the given number
"""

#ask user for an input
numberString = input("Please input a four-digit natural number: ")
errorMessage = "This doesn't seem to be a four-digit natural number"

#check if the input is a four-digit natural number
try:
	numberInteger = int(numberString)
	if numberInteger >= 1000 and numberInteger <= 9999:
		print(f"Awesome, {numberInteger} is a four-digit natural number")
	else:
		print (f"{errorMessage}")
except ValueError:
	print (f"{errorMessage}")

#find the product of the digits of this number
if 'numberInteger' in vars() and numberInteger >= 1000 and numberInteger <= 9999:
	digits = []
	numberIntegerTemp1 = numberInteger			# create a temporary variable for conversion to list

	while numberIntegerTemp1 > 0:
		digits.append(numberIntegerTemp1 % 10)	# get the last digit
		numberIntegerTemp1 //= 10				# remove the last digit
	digits.reverse()							# reverse the list to restore original order

	currentDigit = int(digits[0])
	product = 1

	for currentDigit in digits:
		product *= currentDigit

	print(f"The product of digits {digits} is {product}")

# write the number in reverse order
if 'numberInteger' in vars() and numberInteger >= 1000 and numberInteger <= 9999:
	reverseDigits = list(reversed(digits))
	print(f"{numberInteger} in reverse is {reverseDigits}")

# in ascending order, you need to sort the numbers included in the given number
if 'numberInteger' in vars() and numberInteger >= 1000 and numberInteger <= 9999:
	digitsSortedAsc = list(sorted(digits))
	print(f"{numberInteger} sorted in ascending order is {digitsSortedAsc}")

