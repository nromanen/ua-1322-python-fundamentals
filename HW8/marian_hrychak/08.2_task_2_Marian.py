"""
Write a Python program to check the validity of a password (input from users).
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""

import re


user_input = input("Enter your password: ")


def check_password(password):
    if 6 < len(password) > 16:
        print("Your password must contain at least 6 but no more than 16 characters.")
    elif not re.search("[a-z]", password):
        print("Your password must contain at least one lowercase letter.")
    elif not re.search("[A-Z]", password):
        print("Your password must contain at least one uppercase letter.")
    elif not re.search("[0-9]", password):
        print("Your password must contain at least one number.")
    elif not re.search(r"\W", password):
        print("Your password must contain at least one special character.")
    else:
        print("Password is valid.")

