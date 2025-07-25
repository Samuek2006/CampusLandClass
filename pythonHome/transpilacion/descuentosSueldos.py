"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script calcula el sueldo total de un empleado considerando varios descuentos y aportes.
"""

sueldoBase = float(input("Ingrese el sueldo base del empleado: "))
leyPolitica = sueldoBase * 0.01
segSocial = sueldoBase * 0.04
segForzoso = sueldoBase * 0.05
box_ahorro = sueldoBase * 0.05
amount_total = sueldoBase + leyPolitica + segSocial + segForzoso + box_ahorro

print(f'El monto a descontar a la caja de ahorro es: {box_ahorro:.2f} pesos')
print(f'El monto a descontar por ley de política es: {leyPolitica:.2f} pesos')
print(f'El valor a descontar del seguro forzoso es de: {segSocial:.2f} pesos')
print(f'valor del seguro social: {segForzoso:.2f} pesos')
print(f"El sueldo total del empleado es: {amount_total:.2f} pesos")