"""
Write a program that prompts the user to enter their age, and then
displays a message stating whether the age is even or odd. The program
must provide the ability to enter a negative number, and in this case
generate an exception. The master code should call a function that
processes the information entered.
"""

from even_odd import check_number

"""This is the master code, that accepts data from the user,
processes it, and displays the result."""

if __name__ == '__main__':
    user_age = int(input("Enter your age: "))
    while True:
        check_number(user_age)
        break
