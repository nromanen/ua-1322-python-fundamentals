numbers = [7, 3, 1, 9, 2, 6, 8, 4, 10, 5]
correct_login  = "First"

def task1(my_list):
    div_by_2 = []  
    div_by_3 = []  
    div_not_by_2_or_3 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            div_by_2.append(my_list[i])
        elif my_list[i] % 3 == 0:
            div_by_3.append(my_list[i])
        else:
            div_not_by_2_or_3.append(my_list[i])
    return div_by_2, div_by_3, div_not_by_2_or_3

div_by_2, div_by_3, div_not_by_2_or_3 = task1(numbers)  
print(f"Числа які діляться на 2: {div_by_2}")
print(f"Числа які  діляться на 3: {div_by_3}")
print(f"Числа які не діляться на 2 і на 3: {div_not_by_2_or_3}")



def task2(login):
    while True:
        user_login = input("Введітьб логін: ")
        if login == user_login:
            print("Вітаємо користувачу")
            break
        else:
            print("Помилка")
            

task1(numbers)
task2(correct_login)