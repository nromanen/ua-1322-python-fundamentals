class MyError(Exception):
    def __init__(self, data):
        self.data = data


def number_day(number):
    """ It's a function that gives the day of the week that corresponds to the entered number
    (1 is Monday, 2 is Tuesday, etc.). It raises an error from class MyError if entered numbers are
    negative or from 8 and more and excepts it. It also excepts ValueError if entered nonnumerical
    data or float numbers."""
    try:
        if int(number) <= 0 or int(number) > 7:
            raise MyError(f'wrong number {number}')
        match number:
            case '1': return 'Monday'
            case '2': return 'Tuesday'
            case '3': return 'Wednesday'
            case '4': return 'Thursday'
            case '5': return 'Friday'
            case '6': return 'Saturday'
            case '7': return 'Sunday'
    except MyError as e:
        return e
    except ValueError:
        return f'wrong data: {number}'


# It's a master code that prompts the users to enter the number and calls a function
# that gives the day of the week that corresponds to the entered number
if __name__ == '__main__':
    while True:
        number_input = input('Enter number "1-7" or "q" to exit: ')
        if number_input != 'q':
            print(number_day(number_input))
        else:
            print('Good by!')
            break
