number = input("Please enter a four-digit number: ")

if len(number) != 4:
    print("Please enter a four-digit number.")
else:
    #task 1
    product = 1
    for digit in number:
        product *= int(digit)
        
    #task 2
    reversed_number = number[::-1]
    
    #task 2
    sorted_number = ''.join(sorted(number))

    # print results
    print("The product of the digits:", product)
    print("The number in reverse order:", reversed_number)
    print("The numbers in ascending order: ", sorted_number)
