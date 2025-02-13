import re


def validate(password_user):
    pat_letter = "[a-zA-Z]"
    pat_num = "\d"
    pat_spec = "[$#@]"
    result = True
    if not re.findall(pat_letter, password_user):
        print("Password does not have 1 letter between [a-z,A-Z]")
        result = False
    if not re.findall(pat_num, password_user):
        print("Password does not have 1 number between [0-9]")
        result = False
    if not re.findall(pat_spec, password_user):
        print("Password does not have 1 character from [$#@]")
        result = False
    if not len(password_user) >= 6 or not len(password_user) <= 16:
        print(f"Password password length must be from 6 to 16 characters, but has {len(password_user)}")
        result = False
    return result


while True:
    password_user = input("Enter password: ")
    if validate(password_user):
        print("Hello")
        break
