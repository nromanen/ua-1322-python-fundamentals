def is_lower(i):
    if any(char.islower() for char in i):
        return True 
    return False  

def is_upper(i):
    if any(char.isupper() for char in i):
        return True
    return False

def is_number(i):
    if any(char.isnumeric() for char in i):
        return True
    return False

def right_length(i):
    if 6 <= len(i) <= 16:
        return True
    return False

def is_special(i):
    specials = ["$", "#", "@"]
    if any(char in specials for char in i):
        return True
    return False