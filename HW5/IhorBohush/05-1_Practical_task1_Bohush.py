# Create a list that contains elements of integer type, then use
# the loop to change the type of these elements to a floating type.
lst = [0, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 0]
for el in range(len(lst)):
    lst[el] = float(lst[el])
print(lst)
