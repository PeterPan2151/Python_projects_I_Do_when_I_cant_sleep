temperatures_fahrenheit = [32, 50, 77, 100, 212]
converted_temps = [((i - 32) * 5/9) for i in temperatures_fahrenheit]
print(f'Temperatures in Fahrenheit: {temperatures_fahrenheit}')
print(f'Temperarures in Celsius: {converted_temps}')