"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script realiza la clasificación de triángulos según sus lados.
"""

lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

if (lado1 == lado2) and (lado2 == lado3):
    print("El triángulo es equilátero.")
elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
