# Функція для обчислення площі прямокутника
def area_of_rectangle(length, width):
    return length * width

# Функція для обчислення площі трикутника
def area_of_triangle(base, height):
    return 0.5 * base * height

# Функція для обчислення площі кола
def area_of_circle(radius):
    return math.pi * radius ** 2

def main():
    print("Оберіть фігуру для обчислення площі:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")
    
    choice = int(input("Введіть номер вашого вибору: "))
    
    if choice == 1:
        length = float(input("Введіть довжину прямокутника: "))
        width = float(input("Введіть ширину прямокутника: "))
        area = area_of_rectangle(length, width)
        print(f"Площа прямокутника: {area} квадратних одиниць.")
        
    elif choice == 2:
        base = float(input("Введіть основу трикутника: "))
        height = float(input("Введіть висоту трикутника: "))
        area = area_of_triangle(base, height)
        print(f"Площа трикутника: {area} квадратних одиниць.")
        
    elif choice == 3:
        radius = float(input("Введіть радіус кола: "))
        area = area_of_circle(radius)
        print(f"Площа кола: {area} квадратних одиниць.")
        
    else:
        print("Невірний вибір! Будь ласка, виберіть 1, 2 або 3.")

# Викликаємо головну функцію для запуску програми
if __name__ == "__main__":
    main()
