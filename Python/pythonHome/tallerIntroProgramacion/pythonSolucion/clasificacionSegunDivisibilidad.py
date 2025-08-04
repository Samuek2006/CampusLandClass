"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script clasifica números según su divisibilidad por 2 y 3.
"""

num = int(input("Ingrese un número entero: "))

if num % 2 == 0 and num % 3 == 0:
    print(f"El número {num} es divisible por 2 y por 3.")
elif num % 2 == 0:
    print(f"El número {num} es divisible por 2 pero no por 3.")
elif num % 3 == 0:
    print(f"El número {num} es divisible por 3 pero no por 2.")
else:
    print(f"El número {num} no es divisible ni por 2 ni por 3.")