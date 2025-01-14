import re

def is_lower(i):
    if re.search(r"[a-z]", i):
        return True 
    return False

def is_upper(i):
    if re.search(r"[A-Z]", i):
        return True
    return False

def is_number(i):
    if re.search(r"\d", i):
        return True
    return False

def is_special(i):
    if re.search(r"[@#$]", i):
        return True
    return False

def right_length(i):
    if 6 <= len(i) <= 16:
        return True
    return False

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