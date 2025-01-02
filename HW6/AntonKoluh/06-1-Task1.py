#Even
print([num for num in range(1, 11) if num % 2 == 0])

#Odd
print([num for num in range(1, 11) if num % 3 == 0])

#Not %2 and not %3
print([num for num in range(1, 11) if num % 3 != 0 and num % 2 != 0])