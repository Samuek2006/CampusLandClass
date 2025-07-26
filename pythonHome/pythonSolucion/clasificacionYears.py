"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script es un conversor de unidades de medida.
"""
year = int(input("Ingrese un año: "))

if (year % 400 == 0) and (year % 100 == 0) and (year % 4 == 0):
    print(f"{year} es un año bisiesto")
elif (year % 400 != 0) and (year % 100 == 0) and (year % 4 == 0):
    print(f"{year} no es un año bisiesto")
elif (year % 100 != 0) and (year % 4 == 0):
    print(f"{year} es un año bisiesto")
else:
    print(f"{year} no es un año bisiesto")