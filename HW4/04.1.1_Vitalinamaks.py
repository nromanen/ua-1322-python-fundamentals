temp_cel=float(input("Enter the temperature in Celsius:"))
if temp_cel<-273.15:
    print(f"Temperature below absolute zero(-273.15°C)")
else:
    temp_fahr=(temp_cel * 9/5) + 32
    print(f"{temp_cel}°C is equivalent to {temp_fahr}°F")