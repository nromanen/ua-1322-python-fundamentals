"""
Write a program that analyzes the entered number and, depending on the
number, gives the day of the week that corresponds to this number (1 is
Monday, 2 is Tuesday, etc.). Take into account cases of entering numbers
from 8 and more, as well as cases of entering non-numerical data.
"""

def give_day(num: int):
    """This function returns the day of the week that corresponds
    to the input number."""
    days_week = {
        1: 'Monday', 2: 'Tuesday',
        3: 'Wednesday', 4: 'Thursday',
        5: 'Friday', 6: 'Saturday',
        7: 'Sunday'
    }

    if not isinstance(num, int):
        raise TypeError('Invalid type.')

    if num > 7:
        raise ValueError('Enter a number from 1 to 7.')

    return f"{num} is {days_week[num]}"

