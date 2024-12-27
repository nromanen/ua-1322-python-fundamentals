cels = float(input("Enter the temperature in Celsius: "))

#Convert a temperature in Celsius to Fahrenheit
fahr = (cels * 9 / 5) + 32

#Check if a temperature in Fahrenheit is not below absolute zero
if cels < -273.15:
    result = f"Temperature below absolute zero ({cels}°C)"
else:
    result = f"{cels}°C is equivalent to {fahr}°F"
#Print appropriate output
print(result)