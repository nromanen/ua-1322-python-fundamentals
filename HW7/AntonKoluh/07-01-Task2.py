#calculate area of triangle, rectangle and circle
PI = 3.14

def triangle_area(base: float, height: float) -> float:
    """Triangle area calculation"""
    return float((base*height)/2)

def rect_area(lenght: float, width: float) -> float:
    """rectangle area calculation"""
    return float(lenght * width)

def circle_area(radius: float) -> float:
    """Circle area calculation"""
    return float(PI*(radius**2))

select_area = input("Please select the shape for area calculation (Choices are: Circle, Rectangle, Triangle): \n").lower()

if select_area == "circle":
    r = float(input("please input the Radius of the circle: "))
    print (f"The area of a circle with a radius of {r} is: {circle_area(r)}")
elif select_area == "rectangle":
    l = float(input("please input the lenght of the rectangle: "))
    w = float(input("please input the width of the rectangle: "))
    print(f"The area of a rectangle with a width of {w} and a lenght of {l} is: {rect_area(l, w)}")
elif select_area == "triangle":
    b = float(input("please input the base of the triangle: "))
    h = float(input("please input the height of the triangle: "))
    print (f"The area of a triangle with a base of {b} and a height of {h} is: {triangle_area(b, h)}")
else:
    print(f"{select_area} is not a valid input.")


