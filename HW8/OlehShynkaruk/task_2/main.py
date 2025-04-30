from geometry import rectangle_area, triangle_area, circle_area

def main():
    print("Choose a figure to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {rectangle_area(a, b)}")
    elif choice == "2":
        h = float(input("Enter the height of the triangle: "))
        a = float(input("Enter the base of the triangle: "))
        print(f"The area of the triangle is: {triangle_area(h, a)}")
    elif choice == "3":
        r = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {circle_area(r)}")
    else:
        print("Invalid choice.")


main()
