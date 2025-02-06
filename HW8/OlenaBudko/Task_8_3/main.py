from utils import *

select_user = int(input("Enter 1- Area of rectangle, 2- Area of triangle or 3- Area of circle: "))
if select_user == 1:
    a = input("Enter side a of rectangle: ")
    b = input("Enter side b of rectangle: ")
    if a and b:
        print(area_rectangle(float(a), float(b)))
    else:
        print("Invalid input data")
elif select_user == 2:
    h = input("Enter hight h of rectangle: ")
    b = input("Enter base b of rectangle: ")
    if h and b:
        print(area_triangle(float(h), float(b)))
    else:
        print("Invalid input data")
elif select_user == 3:
    r = input("Enter radius  of rectangle: ")
    print(area_circle(float(r)))
else:
    print("Enter 1 or 2 or 3")
