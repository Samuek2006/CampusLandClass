"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este script calcula el interes que el banco le da a sus ahorradores por cada mes
"""
saldoInicial = float(input("Ingrese el saldo inicial: "))
meses = int(input("Ingrese el número de meses: "))

monto = (0.015 * saldoInicial) * meses
saldoFinal = saldoInicial + monto
print(f'El saldo final después de {meses} meses es: {saldoFinal}')