"""
Print Fibonacci numbers up to the entered number n, using cycles.
(Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)
"""

fibonacci_list = [0, 1]                                  # starting fibonacci list
last_number = int(input("enter the last number "))       # ask for the last number

while True:                                              # create an infinite loop
	x = (fibonacci_list[-1] + fibonacci_list[-2])        # variable x = sum of the last two numbers
	if x <= last_number:                                 # condition that compares x to the last number
		fibonacci_list.append(x)                         # if x <= last number, add it to the list
	else:                                                # otherwise, break the loop
		break

print(fibonacci_list)                                    # print the result
