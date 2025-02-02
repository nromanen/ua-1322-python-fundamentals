import re


def valid_password(password):
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
        return "Password is valid"
    return '\n'.join(invalid_password)


if __name__ == '__main__':
    while True:
        pass_word = input('Create valid password: ')
        print(valid_password(pass_word))
        if valid_password(pass_word) == 'Password is valid':
            break
