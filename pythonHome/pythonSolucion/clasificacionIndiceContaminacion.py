"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script clasifica el índice de contaminación del aire.
"""

ICA = float(input("Ingrese el Índice de Calidad del Aire (ICA): "))

if ICA >= 0 and ICA <= 50:
    print("Clasificación: Buena calidad del aire")
elif ICA > 50 and ICA <= 100:
    print("Clasificación: Moderada calidad del aire")
elif ICA > 100 and ICA <= 150:
    print("Clasificación: No saludable para grupos sensibles")
elif ICA > 150 and ICA <= 200:
    print("Clasificación: No saludable")
elif ICA > 200 and ICA <= 300:
    print("Clasificación: Muy no saludable")
elif ICA > 300:
    print("Clasificación: Peligrosa")
else:
    print("Valor del ICA no válido. Debe ser un número positivo.")