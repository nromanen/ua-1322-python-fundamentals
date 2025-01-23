from functions import rectangle_area, triangle_area, circle_area

while True:
    figure = input("Enter the figure (rectangle, triangle or circle): ").lower()
    match figure:
        case "rectangle":
            width = float(input("Enter the width: "))
            height = float(input("Enter the height: "))
            print(f"The area of the rectangle is {rectangle_area(width, height)}")
            break
        case "triangle":
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            print(f"The area of the triangle is {triangle_area(base, height)}")
            break
        case "circle":
            radius = float(input("Enter the radius: "))
            print(f"The area of the circle is {circle_area(radius)}")
            break
        case _:
            print("Invalid figure. Enter rectangle, triangle or circle.")