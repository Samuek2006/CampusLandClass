"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: porcentaje de inversión de tres personas
"""

inv1 = float(input('Ingresa la cantidad a invertir de la persona 1'))
inv2 = float(input('Ingresa la cantidad a invertir de la persona 2'))
inv3 = float(input('Ingresa la cantidad a invertir de la persona 3'))
invTotal = (inv1 + inv2 + inv3)
p1 = (inv1 * 100)/invTotal
p2 = (inv2 * 100)/invTotal
p3 = (inv3 * 100)/invTotal

print(f'El porcentaje que invierte la 1ra persona es de: {p1}%')
print(f'El porcentaje que invierte la 2da persona es de: {p2}%')
print(f'El porcentaje que invierte la 3ra persona es de: {p3}%')
