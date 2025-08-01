"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script clasifica la edad ingresada en diferentes categorías: niño, adolescente, adulto o adulto mayor.
"""

edad = int(input("Ingrese su edad: "))
if ( edad > 0 ) and ( edad <= 12):
    print ("Usted es un niño")
elif ( edad > 12 ) and ( edad <= 17 ):
    print ("Usted es un adolescente")
elif ( edad > 17 ) and ( edad <= 59 ):
    print ("Usted es un adulto")
else:
    print ("Usted es un adulto adulto mayor")