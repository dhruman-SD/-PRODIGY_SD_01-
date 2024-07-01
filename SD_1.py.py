Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def celsius_to_fahrenheit(celsius):
...     return (celsius * 9/5) + 32
... 
... def celsius_to_kelvin(celsius):
...     return celsius + 273.15
... 
... def fahrenheit_to_celsius(fahrenheit):
...     return (fahrenheit - 32) * 5/9
... 
... def fahrenheit_to_kelvin(fahrenheit):
...     return (fahrenheit - 32) * 5/9 + 273.15
... 
... def kelvin_to_celsius(kelvin):
...     return kelvin - 273.15
... 
... def kelvin_to_fahrenheit(kelvin):
...     return (kelvin - 273.15) * 9/5 + 32
... 
... 
... print("Temperature Converter")
... 
... while True:
...     
...     temp_value = float(input("Enter a temperature value: "))
...     temp_unit = input("Enter the original unit of measurement (C, F, or K): ")
... 
...    
...     if temp_unit.upper() == "C":
...         fahrenheit = celsius_to_fahrenheit(temp_value)
...         kelvin = celsius_to_kelvin(temp_value)
...         print(f"{temp_value}°C is equivalent to {fahrenheit}°F and {kelvin}K")
...     elif temp_unit.upper() == "F":
...         celsius = fahrenheit_to_celsius(temp_value)
...         kelvin = fahrenheit_to_kelvin(temp_value)
...         print(f"{temp_value}°F is equivalent to {celsius}°C and {kelvin}K")
...     elif temp_unit.upper() == "K":
...         celsius = kelvin_to_celsius(temp_value)
...         fahrenheit = kelvin_to_fahrenheit(temp_value)
...         print(f"{temp_value}K is equivalent to {celsius}°C and {fahrenheit}°F")
...     else:
        print("Invalid unit of measurement. Please try again.")

    
    response = input("Do you want to convert another temperature? (y/n): ")
    if response.lower()!= "y":
        break

