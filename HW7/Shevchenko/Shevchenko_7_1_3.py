def calc(msg):
    a = {}
    
    for i in msg:
        keys = a.keys()
        
        if i in keys:
            a[i] += 1
        else:
            a[i] = 1
    return a

str = input('Введіть слово: ')
c = calc(str)
print(c)        