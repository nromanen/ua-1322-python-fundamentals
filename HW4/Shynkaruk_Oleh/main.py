def temperature_converter(temp):
    temp = float(temp)
    result = (temp * 9/5) + 32
    return print("Error: Temperature below absolute zero (-273.15°C)" if temp < -273.15 else f"{temp}°C is equivalent to {result}°F")

temp = input("Enter the temperature in Celsius: ")
temperature_converter(temp)
