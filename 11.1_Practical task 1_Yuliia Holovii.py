def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return "even" if age % 2 == 0 else "odd"

def main():
    try:
        age = int(input("Enter your age: "))
        result = check_age(age)
        print(f"Your age is {result}.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()