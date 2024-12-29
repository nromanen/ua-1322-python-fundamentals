temp_cel=float(input("Enter the temperature in Celsius"))
temp_fahr=(temp_cel * 9/5) + 32
if temp_cel<-273.15:
    print(f"Temperature below absolute zero(-273.15°C)")
else:
    print(f"{temp_cel}°C is equivalent to {temp_fahr}°F")