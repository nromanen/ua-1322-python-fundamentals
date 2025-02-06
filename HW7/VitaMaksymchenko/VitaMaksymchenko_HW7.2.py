choice=input(
    "Select the shape whose area you want to calculate:\n"
    "1 - Rectangle\n"
    "2 - Triangle\n"
    "3 - Circle\n"
)

def area_rectangle():
    a=int(input("Enter width: "))
    b=int(input("Enter length: "))
    s=a*b
    print(f"The area of rectangle is: {s}")
    
def area_triangle():
    a=int(input("Enter height: "))
    b=int(input("Enter length of 1 side: "))
    s=(a*b)/2
    print(f"The area of rectangle is: {s}")

def area_circle():  
    r=int(input("Enter radius: "))
    p=3.14
    s=2*p*(r**2)
    print(f"The area of circle is: {s}")
    
match choice:
    case "1":
        area_rectangle()
    case "2":
        area_triangle()
    case "3":
        area_circle()
    case _:
        print("Invalid choice! Please select 1, 2, or 3.")