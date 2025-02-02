Celsius = float(input("Enter the temperature in Celsius: "))
if Celsius < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    Fahrenheit = (Celsius * 9/5) + 32
print (f"{Celsius}°C is equivalent to {Fahrenheit}°F")