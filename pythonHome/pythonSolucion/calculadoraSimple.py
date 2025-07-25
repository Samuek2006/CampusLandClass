"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script realiza operaciones básicas de una calculadora.
"""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = int(0)
resta = int(0)
multiplicacion = int(0)
division = float(0)

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta  }")
print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
print(f"La división de {num1} y {num2} es: {division}")