import re


def validate(password_user):
    pat_letter = "[a-zA-Z]"
    pat_num = "[\d]"
    pat_spec = "[$#@]"
    if not re.findall(pat_letter, password_user):
        print("Password does not have 1 letter between [a-z,A-Z]")
        return False
    if not re.findall(pat_num, password_user):
        print("Password does not have 1 number between [0-9]")
        return False
    if not re.findall(pat_spec, password_user):
        print("Password does not have 1 character from [\$#@]")
        return False
    if not len(password_user) >= 6 or not len(password_user) <= 16:
        print(f"Password password length must be from 6 to 16 characters, but has {len(password_user)}")
        return False
    return True


while True:
    password_user = input("Enter password: ")
    if validate(password_user):
        print("Hello")
        break
