"""
Task2. Write a script that checks the login that the user enters.
If the login is "First", then greet the users. If the login is
different, send an error message.
(need to use loop while)
"""

login = input("Please enter your login: ")
username = "First"

while login != username:
	login = input(str("Login is incorrect, please try again: "))

print (f"Welcome, {username}!")