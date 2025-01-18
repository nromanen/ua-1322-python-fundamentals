import re


def valid_password():
    while True:
        password = input('Create valid password: ')
        invalid_password = []

        # Check for length
        if len(password) < 6 or len(password) > 16:
            invalid_password.append('Must be at least 6 characters and no more than 16 characters.')

        # Check for the special characters
        if not re.search("[a-z]", password):
            invalid_password.append('Must contain at least one lowercase letter.')
        if not re.search("[A-Z]", password):
            invalid_password.append('Must contain at least one uppercase letter.')
        if not re.search(r"\d", password):
            invalid_password.append('Must contain at least one digit.')
        if not re.search("[$#@]", password):
            invalid_password.append('Must contain at least one special character from [$#@].')
        if len(invalid_password) == 0:
            break
        invalid_password = '\n'.join(invalid_password)
        print(f"Invalid password:\n{invalid_password}")
        continue
    return "Password is valid"
