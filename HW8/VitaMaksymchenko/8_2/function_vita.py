def has_lowercase(s): #condition 1
    return any(char.islower() for char in s)

def has_uppercase(s): #condition 1
    return any(char.isupper() for char in s)

def has_digit(s): #condition 2
    return any(char.isdigit() for char in s)

def has_special_char(s): #condition 3
    return any(char in "$#@" for char in s)

def is_valid_length(s): #condition 4,5
    return 6 <= len(s) <= 16