import math
n = int(input('Enter integer number n = '))
# Use a loop to check if the entered number is >= 0.
# If it is < 0 print "Wrong number", if not - continue the loop.
while n >= 0:
    # Input data for the next loop to calculate the factorial of the entered
    # number
    number = 1
    n1 = 1
    factorial = 1
    while number <= n:
        factorial = number * n1
        number += 1
        n1 = factorial
    print(f'{n} != {factorial}')
    break
else:
    print('Wrong number')


# Another way
# Use a loop to check if the entered number is >= 0.
# If it is < 0 print "Wrong number", if not - continue the loop.
while n >= 0:
    # Input data for the next loop to calculate the factorial of the entered
    # number
    number = 1
    factorial = []
    while number <= n:
        factorial.append(number)
        number += 1
    print(f'{n} != {math.prod(factorial)}')
    break
else:
    print('Wrong number')
