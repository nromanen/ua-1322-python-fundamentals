import math
# The first way
number = input('Enter four-digit natural number: ')
number1 = [int(number[0]), int(number[1]), int(number[2]), int(number[3])]
num = sorted(number1)
print(
    f"product: {number1[0] * number1[1] * number1[2] * number1[3]}",
    f"reverse order: {number1[3]}{number1[2]}{number1[1]}{number1[0]}",
    f"sorted: {num[0]}{num[1]}{num[2]}{num[3]}",
    sep='\n'
)

# Another way
num1 = math.prod(number1)
num2 = list(reversed(number1))
num3 = sorted(number1)
print(
    f"product: {num1}",
    f"reverse order: {num2[0]}{num2[1]}{num2[2]}{num2[3]}",
    f"sorted: {num3[0]}{num3[1]}{num3[2]}{num3[3]}",
    sep='\n'
)
