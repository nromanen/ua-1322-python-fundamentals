"""Task1. Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type.
(Hint: use the built-in float() function)."""

lst = [1, 2, 3, 4, 5]
for i in range(len(lst)):
    lst[i] = float(lst[i])

"""Task2. Print Fibonacci numbers up to the entered number n, using cycles.
(Sequence of Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, etc.)"""

n = int(input("Enter the number: "))
fib1 = 0
fib2 = 1
print(f"Fibonacci numbers up to the entered number: {n}")
while fib1 <= n:
    print(fib1, end=" ")
    fib1, fib2 = fib2, fib1 + fib2  

"""Task3. Write a script that will calculate the factorial of the entered number without using recursion.
Example:
0! = 1, 1! = 1, 2! = 2, 3! = 1 × 2 × 3 = 6, ...."""

n = int(input("Enter the number: "))
i = 1
factorial = 1
while i <= n:
    factorial *= i
    i += 1
print(f"{n}! = {factorial}")


