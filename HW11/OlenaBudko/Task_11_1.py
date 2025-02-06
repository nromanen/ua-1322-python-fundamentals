# Task 1
def even_odd(age):
    if age > 0:
        if age % 2 == 0:
            print(f"Age {age} is even")
        else:
            print(f"Age {age} is odd")
        return True
    else:
        raise ValueError("That is not a positive number!")


# Task 2
res = False
while not res:
    try:
        number = input("Enter day's number from 1 to 7: ")
        if not number.isnumeric():
            raise TypeError("Non-numerical data input")
        number = int(number)
        if number < 1 or number > 7:
            raise ValueError("Number is not from 1 to 7")
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print(week[number - 1])
    except (ValueError, TypeError) as ex:
        print(f"Got exception: {ex}")
