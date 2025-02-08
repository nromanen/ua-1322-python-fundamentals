# Task_1
def max_number(a, b):
    """ Calculate the largest number """
    return a if a > b else b


print(max_number(4, 7))


# Task 2
def rectangle():
    a = float(input("Enter first side by rectangle: "))
    b = float(input("Enter second side by rectangle: "))
    print(f"The area of rectangle is: ", a * b)


def triangle():
    h = float(input("Enter height of the triangle: "))
    b = float(input("Enter base of the triangle: "))
    print(f"The area of triangle is: ", 1 / 2 * h * b)


def circle():
    r = float(input("Enter radius of the circle: "))
    print(f"The area of circle is: ", round(3.14 * r ** 2, 3))


select_area = int(input("Select 1) rectangle, 2)triangle 3)circle: "))
if select_area == 1:
    rectangle()
elif select_area == 2:
    triangle()
elif select_area == 3:
    circle()
else:
    print("Invalid input")


# Task 3
def count_character(text):
    result = dict()
    for i in text:
        result[i] = result.get(i, 0) + 1
    return result


a = input("Type any text: ")
if a:
    print(count_character(a))
