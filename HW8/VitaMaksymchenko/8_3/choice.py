while True:
    choice = input(
        "Which shape's area do you want to  calculate?\n\
             rectangle - 1\n\
             triangle  - 2\n\
             circle    - 3\n"
    )
    import areas_vita as f

    match choice:
        case "1":
            a = float(input("Enter the lenght of rectangle: "))
            b = float(input("Enter the width of rectangle: "))
            s = f.rectangle_area(a, b)
            print(f"The area of rectangle is: {s}")
            break
        case "2":
            a = float(input("Enter the base of the triangle: "))
            h = float(input("Enter the height of the triangle: "))
            s = f.triangle_area(a, h)
            print(f"The area of the triangle is: {s}")
            break
        case "3":
            r = float(input("Enter the radius of the circle: "))
            from math import pi
            s = f.circle_area(r)
            print(f"Area of the circle is: {s}")
            break
        case _:
            print("Your choice is invalid. Please enter 1, 2 or 3.")
