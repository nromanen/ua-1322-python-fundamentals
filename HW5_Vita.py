# 1 task
list_int = [10, 2, 30, 5, 9, 8, 60, 90, 90]
print(list_int)
list_float = [float(i) for i in list_int]
print(list_float)


# 2 task
n = int(input("Enter stop number for Fibonacci: "))
a = 0
b = 1
if n <= 0:
    print("Enter number below zero")
else:
    print("Fibonacci numbers up to", n, ":")
    while a <= n:
        print(a, end=",")
        a, b = b, a + b
print()

# 3 task
number = int(input("Enter number: "))
if number < 0:
    print("Enter number below zero")
elif number == 0:
    print(f"Factorial of {number}: 1")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"Factorial of {number}: {factorial}")
