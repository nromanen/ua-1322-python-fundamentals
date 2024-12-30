temp_c = float(input("Enter temperature in C: "))

print ("Cannot be below -273.15C" if temp_c < -273.15 else "The temperature in F is: " + round(((temp_c*9/5)+32), 2))