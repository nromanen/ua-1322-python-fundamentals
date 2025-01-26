def age_status(age):
    """This function processes the information to check is the user's age even or odd number.
    If a number of the user's age is negative it raises an exception"""
    try:
        age = int(age)
        if age <= 0:
            raise ValueError(f'that is not a positive number: {age}')
        elif age % 2 == 0:
            return 'Your age is an even number'
        else:
            return 'Your age is an odd number'
    except ValueError as e:
        return e


# It's a master code that prompts the users to enter their age and calls a function that
# processes the information entered.
if __name__ == '__main__':
    while True:
        age_input = input('Enter your age or "q" to exit: ')
        if age_input != 'q':
            print(age_status(age_input))
        else:
            break
