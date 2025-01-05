#Task 1
#Determine even numbers that are divisible by 2
a = [x for x in range(1, 10) if x % 2 == 0]
#Determine odd numbers, which are divisible by 3
b = [x for x in range(1, 10) if x % 2 == 1 and x % 3 == 0]
#Determine numbers that are not divisible by 2 and 3
c = [x for x in range(1, 10) if x % 2 != 0 and x % 3 != 0]
#Print the results
print(a)
print(b)
print(c)

#Task 2
login = None
#Take input and check if it's correct
while login != "First":
    login = input("Enter your login: ")
    if login == "First":
        print("Welcome!")
        break
    else:
        print("Wrong login. Try again.")