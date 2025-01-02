print("Numbers that are divisible by 2: ", end="")
for i in range(1, 10):
    if i % 2 == 0:
        print(i, end=" ")
print()
print("Numbers that are divisible by 3: ", end="")
for i in range(1, 10):
    if i % 3 == 0:
        print(i, end=" ")
print()
print("Numbers that are not divisible by 2 and 3: ", end="")
for i in range(1, 10):
    if i % 3 != 0 and i % 2 != 0:
        print(i, end=" ")
