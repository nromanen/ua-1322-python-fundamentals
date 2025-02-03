"""
In the range from 1 to 10 determine
• even numbers that are divisible by 2,
• odd numbers, which are divisible by 3,
• numbers that are not divisible by 2 and 3.
"""

even_numbers = []
odd_numbers = []
not_divisible_numbers = []

for digit in range(1, 11):
    if digit % 2 == 0:
        even_numbers.append(digit)
    elif digit % 3 == 0:
        odd_numbers.append(digit)
    else:
        not_divisible_numbers.append(digit)

print(f"Even numbers: {', '.join(map(str, even_numbers))}.",
      f"Odd numbers: {', '.join(map(str, odd_numbers))}.",
      f"Not divisible numbers: {', '.join(map(str, not_divisible_numbers))}.",
      sep='\n')
