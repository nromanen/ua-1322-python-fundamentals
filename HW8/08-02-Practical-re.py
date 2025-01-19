import re

def check(paswd: str) -> bool:
    re_pattern = r"(?=.*[#$@]+)(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[0-9]+)"
    if re.search(re_pattern, paswd) and len(paswd) >= 6 and len(paswd) <= 16:
        return True
    else:
        return False
    

if __name__ == "__main__":
    paswd_input = str(input("Enter a password that is atleast 6 chars in lenght with a max of 16, atleast 1 letter, number and special char($#@):\n"))
    print (paswd_input + " is valid" if check(paswd_input) else "invalid")