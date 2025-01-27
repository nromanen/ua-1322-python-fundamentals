""""Task1. In the range from 1 to 10 determine

even numbers that are divisible by 2,
odd numbers, which are divisible by 3,
numbers that are not divisible by 2 and 3."""

numbers_range = range(1, 11)
even_nums = [i for i in numbers_range if i%2==0]
print(even_nums)
odd_nums = [i for i in numbers_range if i%3==0]
print(odd_nums)
not_divisible = [i for i in numbers_range if i%2!=0 and i%3!=0]
print(not_divisible)
