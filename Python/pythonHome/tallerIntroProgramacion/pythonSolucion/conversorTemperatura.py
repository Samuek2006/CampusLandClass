"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script un conversor de temperatura.
"""

temperatura = float(input('Ingrese la temperatura: '))
unidadOrigen = input('Ingrese la unidad origen de temperatura:(c,f) ').upper()
if (unidadOrigen == "C"):
    conversion = (temperatura * 9/5) +32
    print('El resultado de la conversion de Celsius a Fahrenheit es:', conversion)
else:
    conversion = (temperatura -32) * 5/9
    print('El resultado de la conversion de Fahrenheit a Celsius es:', conversion)