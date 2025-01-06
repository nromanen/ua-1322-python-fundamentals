#Function that returns the largest of 2 number

def larger_num(num1: int, num2: int) -> int:
    """
    Calculate the bigger number
    """
    return num1 if num1 > num2 else num2

print(larger_num(2,3))