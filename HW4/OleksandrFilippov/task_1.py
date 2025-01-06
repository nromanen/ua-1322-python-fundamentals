def temperature_converter():
    celsius = float(input("Enter the temperature in Celsius: "))
    if celsius < -273.15:
        print(f"Error: Temperature below absolute zero (-273.15C)")
    else:
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}C is equivalent to {fahrenheit}F")
temperature_converter()