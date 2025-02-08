from shapes import rectangle_area, triangle_area, circle_area
import math

def main():
    print("Choose the figure to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    choice = int(input("Enter the number of your choice: "))
    
    if choice == 1:
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        area = rectangle_area(a, b)
        print(f"The area of the rectangle is: {area}")
    
    elif choice == 2:
        a = float(input("Enter the base of the triangle: "))
        h = float(input("Enter the height of the triangle: "))
        area = triangle_area(a, h)
        print(f"The area of the triangle is: {area}")
    
    elif choice == 3:
        r = float(input("Enter the radius of the circle: "))
        area = circle_area(r)
        print(f"The area of the circle is: {area}")
    
    else:
        print("Invalid choice. Please choose a valid figure.")

if __name__ == "__main__":
    main()
