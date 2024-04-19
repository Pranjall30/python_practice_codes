#Convert celsius temperature in fahrenheit and kelvin

celsius = int(input("Enter the temperature in Celsius: "))

#calculate fahrenheit temperature
fahrenheit_temp = (celsius * 9/5) + 32

#calculate kelvin temperature
kelvin_temp = celsius + 273.15

print(f"The temperature in Fahrenheit is: {fahrenheit_temp}")
print(f"The temperature in Kelvin is: {kelvin_temp}")