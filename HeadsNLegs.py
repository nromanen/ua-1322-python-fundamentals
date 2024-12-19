Heads = int(input("Enter Heads: "))
Legs = int(input("Enter Legs: "))

Parts = (Heads, Legs)
#Quick Math
Cows = int(Parts[1]/2 - Parts[0])
expectedParts = (Cows + Parts[0] - Cows, (Parts[0] - Cows)*2 + Cows*4)

if (expectedParts[0] - Parts[0]) or (expectedParts[1] - Parts[1]) != 0:
    print("Impossible Solution")
else:
    print (f"Chickens:{Parts[0]-Cows} Cows:{Cows}")