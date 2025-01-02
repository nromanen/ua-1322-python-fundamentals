celsius = float(input('Введіть температуру у градусах за Цельсієм: '))
fahrenheit = (celsius * 9/5) + 32

if celsius <= -273.15:
   print('Error: Температура нижче абсолютного нуля (-273.15°C)')
else:
    fahrenheit = round(fahrenheit, 2)
    print(f'{celsius}C дорівнює {fahrenheit}F')
