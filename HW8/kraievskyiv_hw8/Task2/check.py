import functions as f

def check_password():
    errors = []
    while True:
        password = input("Enter your password: ")
        if not f.is_lower(password):
            errors.append("Password must contain at least one lowercase letter.")
        if not f.is_upper(password):
            errors.append("Password must contain at least one uppercase letter.")
        if not f.is_number(password):
            errors.append("Password must contain at least one number.")
        if not f.right_length(password):
            errors.append("Password must contain minimum 6 and maximum 16 characters.")
        if not f.is_special(password):
            errors.append("Password must contain at least one of the following characters: $, #, @.")
    
        if errors:
            for error in errors:
                print(error)
            errors.clear()
        else:
            print("Welcome!")
            break

if __name__ == '__main__':
    check_password()