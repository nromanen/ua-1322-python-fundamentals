import re


def check(paswd: str) -> tuple:
    errors = []
    if len(paswd) > 16 or len(paswd) < 6:
        errors.append("More than 6 chars and less than 16")
    if not re.search(r".*[0-9]+", paswd):
        errors.append("Must contain a number")
    if not re.search(r".*[a-z]+", paswd):
        errors.append("Must contain a lower case")
    if not re.search(r".*[A-Z]+", paswd):
        errors.append("Must contain a upper case")
    if not re.search(r".*[$@#]+", paswd):
        errors.append("Must contain a special character")
    return errors


if __name__ == "__main__":
    paswd_input = str(input("Enter a password that is atleast 6 chars in lenght with a max of 16, atleast 1 letter, number and special char($#@):\n"))
    errors = check(paswd_input)
    print(f"{paswd_input} is valid" if not errors else f"{paswd_input} does not match the follow criteria: \n" + "\n".join(x for x in errors))
