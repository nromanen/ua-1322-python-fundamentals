"""
"Temperature Converter"
Write a Python program that prompts the user to enter a temperature in
Celsius and then converts it to Fahrenheit using the formula:
F = (C * 9/5) + 32. Your program should then print out the converted
temperature in Fahrenheit. However, if the user enters a temperature below
-273.15°C (the lowest possible temperature in the universe, also known
as absolute zero), your program should print an error message instead of
attempting to convert the temperature.

Note: You can assume that the user will enter a valid input (a number for
the temperature in Celsius).

Example output:
Enter the temperature in Celsius: 25
25°C is equivalent to 77°F
Example output (if the user enters a temperature below absolute zero):
Enter the temperature in Celsius: -300
Error: Temperature below absolute zero (-273.15°C).
"""

try:
    input_temperature = input("Enter the temperature in Celsius: ")

    if float(input_temperature) >= -273.15:
        converted_temperature_F = (float(input_temperature) * 9 / 5) + 32
        print(f"Enter the temperature in Celsius: {input_temperature}°C",
              f"{input_temperature}°C is equivalent to {converted_temperature_F}°F.",
              sep='\n')
    else:
        print(f"Enter the temperature in Celsius: {input_temperature}°C")
        print("Error: Temperature below absolute zero (-273.15°C).")

except ValueError:
    print('Error: Invalid input.')
