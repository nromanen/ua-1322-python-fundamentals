import calc_area

def main():
    while True:
        print("\nОберіть фігуру, площу якої бажаєте обчислити:")
        print("1. Прямокутник")
        print("2. Трикутник")
        print("3. Коло")
        print("4. Вихід")

        choice = input("Ваш вибір: ").strip()

        match choice:
            case "1":
                try:
                    a = float(input("Введіть довжину (a): "))
                    b = float(input("Введіть ширину (b): "))
                    area = calc_area.rectangle_area(a, b)
                    print(f"Площа прямокутника: {area}")
                except ValueError:
                    print("Некоректне введення. Спробуйте ще раз.")

            case "2":
                try:
                    a = float(input("Введіть довжину основи (a): "))
                    h = float(input("Введіть висоту (h): "))
                    area = calc_area.triangle_area(a, h)
                    print(f"Площа трикутника: {area}")
                except ValueError:
                    print("Некоректне введення. Спробуйте ще раз.")

            case "3":
                try:
                    r = float(input("Введіть радіус (r): "))
                    area = calc_area.circle_area(r)
                    print(f"Площа кола: {area}")
                except ValueError:
                    print("Некоректне введення. Спробуйте ще раз.")

            case "4":
                print("Завершення роботи.")
                break

            case _:
                print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
