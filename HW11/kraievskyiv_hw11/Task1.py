def odd_or_even(age):
    """
    Check whether the number is odd or even.
    If it's negative, raise Error.
    """
    if age < 0:
        raise ValueError("Age can't be negative")
    if age % 2 == 1:
        return f"{age} is odd."
    else:
        return f"{age} is even."
    
def main():
    """
    Prompt user's age. Based on it call odd_or_even function.
    Ask user to repeat, until age is non-negative.
    """
    while True:
        try:
            age = int(input("Enter your age: "))
            print(odd_or_even(age))
            break
        except ValueError as e:
            print(f"Error: {e}. Try again")

if __name__ == "__main__":
    main()