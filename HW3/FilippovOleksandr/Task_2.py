
def four_digits(number):
    digits = [int(d) for d in str(number)]
    product_number = 1
    for d in digits:
        product_number *= d
    reversed_number_list = digits[::-1]
    reversed_number = ''.join(map(str, reversed_number_list))
    sorted_number_list = sorted(digits)
    sorted_number = ''.join(map(str, sorted_number_list))
    print("\nTask_2 Results:")
    print(f"Product of digits: {product_number}")
    print(f"Reversed number: {reversed_number}")
    print(f"Sorted digits: {sorted_number}")
    return product_number, reversed_number, sorted_number, 

four_digits(4512)