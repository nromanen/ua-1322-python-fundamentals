number=1234

# 1. Product of digits
digits=[int(d) for d in str(number)]
product=1
for digit in digits:
    product *= digit

# 2. Reverse number
reversed_number = int(str(number)[::-1])

# 3. Sort digits
sorted_digits=''.join(sorted(str(number)))

# Output results
print(f"Product of digits:{product}")
print(f"Reversed number:{reversed_number}")
print(f"Sorted digits:{sorted_digits}")