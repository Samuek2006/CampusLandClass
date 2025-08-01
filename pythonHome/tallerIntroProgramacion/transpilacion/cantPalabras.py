"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este script calcula el precio total de un proyecto en función de la cantidad de palabras, centímetros y colores utilizados.
"""

cantPalabras = int(input("Ingrese la cantidad de palabras: "))
cm = float(input("Ingrese cuantos cm hay en total: "))
cantColores = int(input("Escriba cuantos colores se han usado en total: "))

ps = (cantPalabras * 20000)
cms = (cm * 15000)
crs = (cantColores * 25000)

precio = (ps + cms + crs)
print("El precio total es: ", precio)