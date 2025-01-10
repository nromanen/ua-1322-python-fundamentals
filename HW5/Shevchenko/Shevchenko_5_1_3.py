n = int(input('ВВедіть позитивне число: '))
num = 1
while n < 0:
    print('Помилка! ВВедіть позитивне число: ')
    n = int(input('ВВедіть позитивне число: '))

for i in range(1, n+1):
    num = num * i
    
print(num)