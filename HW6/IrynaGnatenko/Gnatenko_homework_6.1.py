"""
Task1. In the range from 1 to 10 determine
• even numbers that are divisible by 2,
• odd numbers, which are divisible by 3,
• numbers that are not divisible by 2 and 3.
"""

even_numbers = []
odd_numbers = []
not_divisible = []

for i in range (1,10):
	if i % 2 == 0:
		even_numbers.append(i)
	else:
		if i % 3 == 0:
			odd_numbers.append(i)
		else:
			not_divisible.append(i)

print(f"even numbers divisible by 2: {even_numbers}")
print(f"odd numbers divisible by 3: {odd_numbers}")
print(f"numbers not divisible by 2 and 3: {not_divisible}")
