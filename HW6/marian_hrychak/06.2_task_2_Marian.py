"""
Write a script that checks the login that the user enters.
If the login is "First", then greet the users. If the login is
different, send an error message.
(need to use loop while)
"""

login = "First"

while True:
    user_login = input("Enter your login: ")
    if user_login == login:
        print("Login is correct!")
        break
    else:
        print("Error. Login is incorrect!")
