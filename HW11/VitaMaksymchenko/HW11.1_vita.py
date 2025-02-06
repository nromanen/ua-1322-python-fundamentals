def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age % 2 == 0:
        print(f"The age {age} is even.")
    else:
        print(f"The age {age} is odd.")


def main():
    while True:
        try:
            age = int(input("Enter your age: "))
            process_age(age)
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid positive age.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
