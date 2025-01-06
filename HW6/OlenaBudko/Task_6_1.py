# Task 1
# Task1. In the range from 1 to 10 determine
# even numbers that are divisible by 2,
# odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3

result1 = [x for x in range(1, 11) if x % 2 == 0]
print(result1)
result2 = [x for x in range(1, 11) if x % 3 == 0]
print(result2)
result3 = [x for x in range(1, 11) if x % 2 == 1 and x % 3 == 1]
print(result3)


# Task 2
# Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is different, send an error message.
# (need to use loop while)

while True:
    login = input("Enter login: ")
    if login == "First":
        print("Welcome!")
        break
    else:
        print("Error: Login failed")
