"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script clasifica figuras geométricas según el número de lados.
"""

lados = int(input("Ingrese el número de lados de la figura geométrica: "))

if lados == 3:
    print("La figura es un triángulo.")
elif lados == 4:
    print("La figura es un cuadrado o un rectángulo.")
elif lados == 5:
    print("La figura es un pentágono.")
elif lados == 6:
    print("La figura es un hexágono.")
elif lados > 6:
    print("Figura no soportada")
else:
    print("No es una figura geométrica válida.")