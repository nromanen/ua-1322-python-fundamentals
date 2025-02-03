user = True
while user:
    user_login = input("Enter your login: ")
    if user_login == 'First':
        print("Hello, First!")
        break 
    else:
      print("Error: Incorrect login. Please try again.") 