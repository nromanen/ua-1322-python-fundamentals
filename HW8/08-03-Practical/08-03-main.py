from area import rect_area, triangle_area, circle_area

shape_select = ""
while shape_select != "q":
    shape_select = str(input("Please select the shape for calculation, choices are Triangle, Circle and Rectangle to quit enter q\n")).lower()
    match shape_select:
        case "triangle":
            b = float(input("Please input the base of the triangle: "))
            h = float(input("Please input the height of the triangle: "))
            print(f"The area of a triangle with base of {b} and height of {h} is {triangle_area(h, b)}")
        case "circle":
            r = float(input("Please input the radius of the circle: "))
            print(f"The area of a circle with a radius of {r} is {circle_area(r)}")
        case "rectangle":
            b = float(input("Please input the base of the rectangle: "))
            h = float(input("Please input the height of the rectangle: "))
            print(f"The area of a rectangle with base of {b} and height of {h} is {rect_area(h, b)}")
        case "q":
            print("Exiting")
        case _:
            print("Incorrect input, try again or use q to exit.")