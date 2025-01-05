#Task 1 
#Create a list of integers
lst = [1, 3, 8, 4, 10, 2, 7]

#Change type from int to float
for i in range(len(lst)):
    lst[i] = float(lst[i])

#Print the changed list
print(lst)


#Task 2
n = int(input("Enter a number: "))

#Create starting fibonacci list
fibonacci = [0, 1]

#Create a loop to add the next number in the list
while fibonacci[-1] < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    #Print the fibonacci list up to entered number
    if fibonacci[-1] > n: 
        break
    else: 
        print(fibonacci[-1])


#Task 3
n = int(input("Enter a number: "))

#Factorial of 0 is 1
if n == 0:
    print(1)
#Calculate factorials of the other numbers 
else:
    for i in range(1, n+1):
        factorial = 1
        for j in range(1, i+1):
            factorial *= j
    print(factorial)