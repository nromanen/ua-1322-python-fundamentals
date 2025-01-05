"""
Print Fibonacci numbers up to the entered number n,
using cycles.
"""

n = int(input("Enter a number: "))

fibonacci = [0, 1]
while fibonacci[-1] < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print(fibonacci)
