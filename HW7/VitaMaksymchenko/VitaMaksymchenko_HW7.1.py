num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
"""
    Determine the largest number between two inputs.
    Input 2 numbers: num1 and num2.
    If,else, operator determine which number of them is greater.
    Returns the larger of the two numbers, or a message if they are equal.
    """


def largest_number():
    if num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    else:
        print(f"NONE, because they're equal")


print(f"Max number of {num1},{num2}: ")
largest_number()
