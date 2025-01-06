n = int(input("Enter a number: "))
lst_fibon = [0, 1]
while lst_fibon[-1] <= n:
    lst_fibon.append(lst_fibon[-1] + lst_fibon[-2])
print(",".join(str(x) for x in lst_fibon[:-1]))
