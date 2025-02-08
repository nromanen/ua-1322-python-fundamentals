n = int(input("Enter the number n: "))
y, z = 0, 1
print("Fibonacci sequence:", end=" ")
while y <= n:
    print(y, end=" ")
    y, z = z, y + z
