numbers = range(1, 11)

even_numbers = [num for num in numbers if num % 2 == 0]

odd_numbers_div_3 = [num for num in numbers if num % 2 != 0 and num % 3 == 0]

not_divisible_by_2_or_3 = [num for num in numbers if num % 2 != 0 and num % 3 != 0]