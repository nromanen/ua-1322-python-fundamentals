def rectangle_area(length, width):
    return length * width  # Area of a rectangle = length × width

def triangle_area(base, height):
    return 0.5 * base * height  # Area of a triangle = 0.5 × base × height

def circle_area(radius):
    return 3.14159 * radius * radius  # Area of a circle = π × radius²

def main():
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    choice = input("Enter the number (1/2/3): ")

    if choice == "1":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"Area of the rectangle: {rectangle_area(length, width)}")
    elif choice == "2":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"Area of the triangle: {triangle_area(base, height)}")
    elif choice == "3":
        radius = float(input("Enter the radius of the circle: "))
        print(f"Area of the circle: {circle_area(radius)}")
    else:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()