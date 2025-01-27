n = int(input('Enter integer number n = '))
# Check whether the entered number is positive and not zero.
# If it is <=0 print "Wrong number", if not - continue.
if n > 0:
    n1 = 0
    n2 = 1
    sequence = [0, 1]
    number = 0
    # Use loop to create Fibonacci sequence.
    while number < n:
        number = sequence[n1] + sequence[n2]
        if number <= n:
            sequence.append(number)
            n1 += 1
            n2 += 1
else:
    sequence = 'Wrong number'
print(sequence)
