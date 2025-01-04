"""
A four-digit natural number is specified:
- find the product of the digits of this number
- write the number in reverse order
- in ascending order, you need to sort the numbers included in the given 
number
"""
from math import prod


natural_number = int(input("Enter a natural number: "))

list_digits = []
for i in str(natural_number):
    list_digits.append(int(i))

print("The product of the digits of this number: ", prod(list_digits))

reverse_number = str(natural_number)[::-1]
print(f"Reverse order: {reverse_number}")

sort_number = list(sorted(reverse_number))
print(f"Sort the numbers: {''.join(sort_number)}")
