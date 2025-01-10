import re

def check_password(word):
    
    p = 0
    while True:

        if (len(word)>16 and len(word)<6):
            p = -1
            break

        elif not re.search("[a-z]", word):
            p = -1
            break

        elif not re.search("[A-Z]", word):
            p = -1
            break

        elif not re.search("[0-9]", word):
            p = -1
            break

        elif not re.search("[$#@]" , word):
            p = -1
            break

       # elif re.search("\s" , word):
        #    p = -1
        #    break

        else:
            p = 0
            print("Valid Password")

            break

    if p == -1:
        print("Not a Valid Password ")

password = input('I need Your Password! ')        
check_password(password)