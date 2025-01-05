"""
Write a script that will calculate the factorial of the entered
number without using recursion.
"""

number = int(input("Enter a number: "))

factorial = 1

if number < 0:
    print(f"{number} is less than zero.")
    quit()
else:
    for i in range(2, number + 1):
        factorial *= i

print(f"The factorial of {number} is {factorial}.")
