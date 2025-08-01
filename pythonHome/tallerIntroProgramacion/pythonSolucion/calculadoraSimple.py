"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script realiza operaciones básicas de una calculadora.
"""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operador = input("Ingrese el operador (+, -, *, /): ")
suma = int(0)
resta = int(0)
multiplicacion = int(0)
division = float(0)

if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    resultado = num1 / num2
else:
    print("Operador no válido")

print(f"El resultado de {num1} {operador} {num2} es: {resultado}")

