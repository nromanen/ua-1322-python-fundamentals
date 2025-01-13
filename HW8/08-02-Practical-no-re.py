def check(paswd: str) -> tuple:
    if not any(x.isalpha() for x in paswd):
        return False, "Must contain atleast 1 character"
    if not any(x.isupper() for x in paswd) or not any(x.islower() for x in paswd):
        return False, "Must contain atleast 1 upper and 1 lower case"
    if len(paswd) > 16 or len(paswd) < 6:
        return False, "Must be atleast 6 characters but not over 16"
    if not any(x.isnumeric() for x in paswd):
        return False, "Must contain atleast 1 number"
    if not paswd.count("$") and not paswd.count("#") and not paswd.count("@"):
        return False, "Must contain atleast 1 special character"
    return True, "_"
    



if __name__ == "__main__":
    paswd_input = str(input("Enter a password that is atleast 6 chars in lenght with a max of 16, atleast 1 letter, number and special char($#@):\n"))
    print (paswd_input + " is valid" if check(paswd_input)[0] else "invalid " + check(paswd_input)[1])
