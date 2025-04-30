def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char in "$#@" for char in password):
        return False

    return True


password = input("Enter your password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
