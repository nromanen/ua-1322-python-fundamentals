login = ""
user = "First"
while login != user:
    login = str(input("Enter username: "))
    print("Wrong User" if login != user else f"Welcome {user}")
