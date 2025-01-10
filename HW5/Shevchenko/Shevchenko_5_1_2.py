n = int(input('Введіть ціле число: '))
num1 = 0
num2 = 1
i = 0

while n <= 0:
    print('Помилка! ВВедіть позитивне число: ')
    n = int(input('ВВедіть позитивне число: '))
    
if n == 1:
    print(num1)
    
elif n == 2:
    print(num1, num2)
    
elif n >= 3:
    while i < n:
        print(num1, " ")
        num_n = num1 + num2
        num1, num2 = num2, num_n
        i += 1
else:
    print('Error')
