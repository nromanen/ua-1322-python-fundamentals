number = int(input("Enter the number: "))
fact = 1
i = 0
result = list()
while i < number:
    i += 1
    next = fact * i
    fact = next
    result.append(f"{i}!={next}")
print(", ".join(result))
