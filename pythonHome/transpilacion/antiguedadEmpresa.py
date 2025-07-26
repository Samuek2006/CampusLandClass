"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script calcula el bono final basado en la cantidad de años ingresada.
"""

years = int(0)
bn1 = int(0)
bnfinal = int(0)

years = int(input("Ingrese la cantidad: "))
if (years >= 1):
    bn1 = 100000
    bnfinal = (years*120000) + bn1
else:
    print("El valor ingresado no es correcto, debe ser mayor o igual a 1")
print("El bono final es: ", bnfinal)