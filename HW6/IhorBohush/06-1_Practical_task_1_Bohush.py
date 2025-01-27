lst = list(range(1, 11))
even = []
odd = []
numbers = []
for number in lst:
    if number % 2 == 0:
        even.append(str(number))
    elif number % 3 == 0:
        odd.append(str(number))
    else:
        numbers.append(str(number))
print(
    f'Even numbers that are divisible by 2: {", ".join(even)}',
    f'Odd numbers that are divisible by 3: {", ".join(odd)}',
    f'Numbers that are not divisible by 2 and 3: {", ".join(numbers)}',
    sep='\n'
)
