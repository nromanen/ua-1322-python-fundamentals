import math
def triangle_area(a, b):
    
    c = a * b / 2
    return c

def rectangle_area(c, d):
    
    
    f = c * d
    return f 

def circle_area(r):
    s = math.pi * math.pow(r, 2)
    s = round(s, 2)
    
    return s

choise = int(input('Якщо хочете порахувати площу трикутника, то введіть: 1 \n площу чотирикутника: 2, площу кола: 3 \n'))
if choise == 1:
    a = int(input('Введіть висоту трикутника h: '))
    b = int(input('Введіть довжину сторони трикутника b(h): '))
    v= triangle_area(a, b)
    print(v)
elif choise == 2:
    c = int(input('Введіть першу сторону прямокутника c: '))
    d = int(input('Введіть другу сторону прямокутника d: '))
    w = rectangle_area(c, d)
    print(w)
elif choise == 3:
    r = int(input('Введіть радіус кола r: '))
    y = circle_area(r)
    print(y)
else:
    print('Ви ввели не вірні дані')
