import function_vita as a 

def validate_password(password):
    if a.has_lowercase(password) and a.has_uppercase(password) and a.has_digit(password) and a.has_special_char(password) and a.is_valid_length(password):
        print("Password is valid.") 
    else:
        print("Password is invalid. Enter right password")
        if not a.has_lowercase(password):  
            print("- At least one lowercase letter (a-z).")
        if not a.has_uppercase(password): 
            print("- At least one uppercase letter (A-Z).")
        if not a.has_digit(password):  
            print("- At least one digit (0-9).")
        if not a.has_special_char(password): 
            print("- At least one special character ($, #, @).")
        if not a.is_valid_length(password): 
            print("- Length must be between 6 and 16 characters.")

password = input("Enter your password: ")
validate_password(password)
