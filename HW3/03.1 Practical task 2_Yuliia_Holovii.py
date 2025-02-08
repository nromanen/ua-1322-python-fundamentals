number=1234
digits = [int(d) for d in str(number)]
product = 1
for digit in digits:
    product *= digit
reversed_number = int(str(number)[::-1])
sorted_digits = ''.join(sorted(str(number)))
print(f"Product of digits:{product}")
print(f"Reversed number:{reversed_number}")
print(f"Sorted digits:{sorted_digits}")