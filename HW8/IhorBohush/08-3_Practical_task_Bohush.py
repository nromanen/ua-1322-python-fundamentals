import area

while True:
    area_in = input('Enter "r", or "t", or "c", or "q" to exit: ')
    match area_in:
        case 'r':
            result = f'Area of the rectangle = {area.rectangle()}'
        case 't':
            result = f'Area of the triangle = {area.triangle()}'
        case 'c':
            result = f'Area of the circle = {area.circle()}'
        case 'q':
            break
        case _:
            result = 'Wrong letter! Try again:'
    print(result)

