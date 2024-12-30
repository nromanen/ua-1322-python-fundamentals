#Convert list of int to float

lst = [1, 5, 2, 6, 21, 65, 12, 56, 12, 97, 86, 73]
for i in range(len(lst)):
    lst[i] = float(lst[i])

print (lst)