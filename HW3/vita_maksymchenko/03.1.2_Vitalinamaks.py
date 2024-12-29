number = int(input("Enter the four-digit number "))

if 1000 <= number <= 9999:  # Перевірка на 4-значність
    product = 1
    for digit in str(number):
        product *= int(digit)  # Множимо поточний добуток на цифру
    print(f"The product of the digits is {product}.")

    # Числа в зворотньому порядку
    reverse_number = str(number)[::-1]
    print(f"Reversed number is {reverse_number}")

    # Перетворюємо на список і сортуємо по зростаючому порядку
    sort_number = sorted(reverse_number)
    print(sort_number)

else:
    print(f"Wrong number! It must be four-digit. ")
