import calc

choise = int(input('Якщо хочете порахувати площу трикутника, то введіть: 1 \n площу чотирикутника: 2, площу кола: 3 \n'))
if choise == 1:
    a = int(input('Введіть висоту трикутника h: '))
    b = int(input('Введіть довжину сторони трикутника b(h): '))
    v = calc.triangle_area(a, b)
    print(v)
elif choise == 2:
    c = int(input('Введіть першу сторону прямокутника c: '))
    d = int(input('Введіть другу сторону прямокутника d: '))
    w = calc.rectangle_area(c, d)
    print(w)
elif choise == 3:
    r = int(input('Введіть радіус кола r: '))
    y = calc.circle_area(r)
    print(y)
else:
    print('Ви ввели не вірні дані')