import math
# Функція для обчислення площі прямокутника
def area_of_rectangle(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Довжина та ширина мають бути додатними числами")
    return length * width

# Функція для обчислення площі трикутника
def area_of_triangle(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Основа та висота мають бути додатними числами")
    return 0.5 * base * height

# Функція для обчислення площі кола
def area_of_circle(radius):
    if radius <= 0:
        raise ValueError("Радіус має бути додатним числом")
    return math.pi * radius ** 2

def main():
    print("Оберіть фігуру для обчислення площі:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")
    
    try:
        choice = int(input("Введіть номер вашого вибору: "))
    except ValueError:
        print("Помилка: Введіть ціле число (1, 2 або 3)")
        return
    
    
    if choice == 1:
        try:
            length = float(input("Введіть довжину прямокутника: "))
            width = float(input("Введіть ширину прямокутника: "))
            area = area_of_rectangle(length, width)
            print(f"Площа прямокутника: {area} квадратних одиниць.")
        except ValueError as e:
            print(f"Помилка: {str(e)}")
        
    elif choice == 2:
        try:
            base = float(input("Введіть основу трикутника: "))
            height = float(input("Введіть висоту трикутника: "))
            area = area_of_triangle(base, height)
            print(f"Площа трикутника: {area} квадратних одиниць.")
        except ValueError as e:
            print(f"Помилка: {str(e)}")
        
    elif choice == 3:
        try:
            radius = float(input("Введіть радіус кола: "))
            area = area_of_circle(radius)
            print(f"Площа кола: {area} квадратних одиниць.")
        except ValueError as e:
            print(f"Помилка: {str(e)}")
        
    else:
        print("Невірний вибір! Будь ласка, виберіть 1, 2 або 3.")

# Викликаємо головну функцію для запуску програми
if __name__ == "__main__":
    main()
