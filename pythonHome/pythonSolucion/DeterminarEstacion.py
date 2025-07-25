"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script Determina la estación del año según el mes ingresado.
"""

mes = int(input("Ingrese el número del mes (1-12): "))
if (mes >= 3) and (mes <= 5):
    print("Es primavera.")
elif (mes >= 6) and (mes <= 8):
    print("Es verano.")
elif (mes >= 9) and (mes <= 11):
    print("Es otoño.")
else:
    print("Es invierno.")