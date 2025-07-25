"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script un conversor de temperatura.
"""

temperatura = float(input("Ingrese la temperatura: "))
celFahrenheit = (temperatura * 9/5) + 32
fahrCelsius = (temperatura - 32) * 5/9

print(f"La temperatura en Fahrenheit es: {celFahrenheit:.2f} °F")
print(f"La temperatura en Celsius es: {fahrCelsius:.2f} °C")