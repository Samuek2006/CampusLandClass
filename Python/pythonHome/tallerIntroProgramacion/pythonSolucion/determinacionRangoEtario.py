"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script determina el rango etario de una persona según su edad.
"""

edad = int(input("Ingrese su edad: "))

if edad > 0 and edad <= 2:
    print("El rango etario es: Bebe")
elif edad > 2 and edad <= 12:
    print("El rango etario es: Niño")
elif edad > 12 and edad <= 19:
    print("El rango etario es: Adolescente")
elif edad > 19 and edad <= 64:
    print("El rango etario es: Adulto")
elif edad > 64:
    print("El rango etario es: Adulto mayor")
else:
    print("La edad ingresada no es válida. Debe ser un número positivo.")
