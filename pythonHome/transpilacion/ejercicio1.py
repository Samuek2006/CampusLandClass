"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este script es para calcular las pulsaciones de una persona que debe tener por cada 10 segundos
"""

edad = float(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (M para hombre, F para mujer): ").upper()

if sexo == "M":
    pulsaciones = (210 - edad) / 10
    print(f"Las pulsaciones cada 10 segundos de un hombre de {edad} años son: {pulsaciones}")
elif sexo == "F":
    pulsaciones = (220 - edad) / 10
    print(f"Las pulsaciones cada 10 segundos de una mujer de {edad} años son: {pulsaciones}")
else:
    print("Sexo no válido. Por favor ingrese M o F.")