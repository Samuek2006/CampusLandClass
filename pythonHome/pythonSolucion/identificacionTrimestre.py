"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script identifica el trimestre de un año dado un mes.
"""

mes = int(input("Ingrese el mes (1-12): "))

if mes >= 1 and mes <= 3:
    print("El trimestre es: Primer trimestre")
elif mes >= 4 and mes <= 6:
    print("El trimestre es: Segundo trimestre")
elif mes >= 7 and mes <= 9:
    print("El trimestre es: Tercer trimestre")
elif mes >= 10 and mes <= 12:
    print("El trimestre es: Cuarto trimestre")
else:
    print("Mes inválido. Debe estar entre 1 y 12.")
