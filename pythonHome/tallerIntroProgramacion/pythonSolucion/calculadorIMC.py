"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script calcula el Índice de Masa Corporal (IMC) y proporciona una clasificación.
"""
peso = float(input("Ingrese su peso en kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))

imc = peso / (estatura ** 2)

print(f"Su IMC es: {imc:.2f}")

if imc < 18.5:
    print("Clasificación: Bajo peso")
elif 18.5 <= imc <= 24.9:
    print("Clasificación: Peso normal")
elif 25 <= imc <= 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")
