c_temper = float(input('Enter the temperature in Celsius: '))

if c_temper >= -273.15:
    f_temper = (c_temper * (9 / 5)) + 32
    result = (f'Enter the temperature in Celsius {c_temper}\n'
              f'{c_temper}{chr(176)}C is equivalent to {f_temper}{chr(176)}F')
else:
    result = f'Error: temperature below absolute zero (-273.15)C'
print(result)
