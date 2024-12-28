celsius = float(input('Enter the temperature in Celsius: '))
if celsius >= -273.15:
    fahrenheit = (celsius * 9 / 5) + 32
    result = f'{celsius}°C is equivalent to {fahrenheit}°F'
else:
    result = f'Error: Temperature below absolute zero (-273.15°C)'
print(result)
