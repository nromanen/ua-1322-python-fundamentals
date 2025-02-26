def check_number(num: int):
    """This function checks if the number is even or odd."""
    if num < 0:
        raise ValueError ("Age cannot be negative.")
    print("Even.") if num % 2 == 0 else print("Odd.")

