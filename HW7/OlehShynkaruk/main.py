def find_largest_number(num1, num2):
    """find a largest number

    Args:
        num1 (int or float): first number
        num2 (int or float): second number
    """
    
    print(num1 if num1 > num2 else num2)


def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle(radius):
    return 3.14 * radius ** 2

def main():
    print("Select a shape to calculate the area of:")
    print("1.Rectangle")
    print("2.Triangle")
    print("3.Circle")
    
    choice = input("Choose: (1/2/3): ")
    
    match choice:
        case "1":
            length = float(input("Input length: "))
            width = float(input("Input width: "))
            print("Result: ", rectangle_area(length, width))
        case 2:
            base = float(input("Input base: "))
            height = float(input("Input height: "))
            print("Result: ", triangle_area(base, height))
        case "3":
            radius = float(input("Input radius: "))
            print("Reuslt: ", circle(radius))


def character_count(input_str):
    character = {}
    for char in input_str:
        character[char] = character.get(char, 0) + 1
    return character


result = character_count('hello')
print(result)