import re

def is_lower(i):
    return True if re.search(r"[a-z]", i) else False

def is_upper(i):
    return True if re.search(r"[A-Z]", i) else False

def is_number(i):
    return True if re.search(r"\d", i) else False

def is_special(i):
    return True if re.search(r"[@#$]", i) else False

def right_length(i):
    return True if 6 <= len(i) <= 16 else False

def check_password():
    errors = []
    while True:
        password = input("Enter your password: ")
        if not is_lower(password):
            errors.append("Password must contain at least one lowercase letter.")
        if not is_upper(password):
            errors.append("Password must contain at least one uppercase letter.")
        if not is_number(password):
            errors.append("Password must contain at least one number.")
        if not right_length(password):
            errors.append("Password must contain minimum 6 and maximum 16 characters.")
        if not is_special(password):
            errors.append("Password must contain at least one of the following characters: $, #, @.")

        if errors:
            for error in errors:
                print(error)
            errors.clear()
        else:
            print("Welcome!")
            break

check_password()