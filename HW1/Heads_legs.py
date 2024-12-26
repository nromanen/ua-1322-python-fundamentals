# Запитуємо ввести кількість голів і кількість ніг
heads = input('Input number of the heads: ')
legs = input('Input number of the legs: ')

# Переводимо дані із "str" в "int"
heads = int(heads)
legs = int(legs)

# Перевіряємо введені дані
# Якщо кількість ніг чи голів від'ємна або рівна 0 - виводимо "Немає розв'язків"
if heads < 0 or legs < 0:
    print('No solutions')
# Якщо кількість ніг і голів дорівнює 0, то відповідно кількість курей має бути 0 і корів - 0
elif heads == 0 and legs == 0:
    chickens = 0
    cows = 0
    animals = (chickens, cows)
    print(animals)
# Якщо кількість ніг або голів дорівнює 0, то виводимо "Немає розв'язків"
elif heads == 0 or legs == 0:
    print('No solutions')
# Якщо всі числа більші нуля рахуємо по формулі: cows = (legs - 2 * heads) / 2; chickens = heads - cows
else:
    x = (legs - 2 * heads)
# Перевіряємо цю частину формули чи не від'ємне значення, якщо від'ємне - виводимо "Немає розв'язків"
    if x < 0:
        print('No solutions')
# Далі перевіряємо остачу від ділення на 2
    else:
        y = x % 2
# Якщо остача не дорівнює 0 - виводимо "Немає розв'язків"
# Якщо остача дорівнює 0 - продовжуємо розв'язувати задачу
        if y == 0:
            cows = int(x / 2)
            chickens = heads - cows
# Якщо кількість курей від'ємна - виводимо "Немає розв'язків"
            if chickens < 0:
                print('No solutions')
# Всі інші значення додаємо в кортеж і виводимо отримані значення
            else:
                animals = (chickens, cows)
                print(animals)
        else:
            print('No solutions')
