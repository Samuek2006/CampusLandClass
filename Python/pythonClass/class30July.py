"""
Autor: Samuel Felipe Calderon Soto
Fecha: 30 / 07 2025
Descripcion: Funciones
Tema:
"""
#Comentario en Linea
"""
Funciones:
    - def: Define una funcion

Palabras reservadas:
    - return: Devuelve el valor de una funcion
    - none: Valor por defecto de una funcion
    - Optional: Valor por defecto de una funcion
"""

import os
def suma(n,b):
    return n + b

print(suma(5, 3))


"""Ejercicio 1:
crear un programa que me permita registar N cantidad de aspirantes, al programa de formacion de C#
"""
os.system('cls')
aspirantes = []
rtas = ['S', 's']
isAddStudent = True

def addStudent(name : str):
    aspirantes.append(name, [], [], [])
    print(f'Student {name} agregado Exitosamente.')
    input('Presione Enter para continuar...')

def ShowStudents(std : list):
    os.system('cls')
    for idx, aspirantes in enumerate(std):
        print(f'Aspirante {idx + 1}: {aspirantes}')
    input('Presione Enter para continuar...')

while isAddStudent:
    os.system('cls')
    name = input("Ingrese el nombre del aspirante: ")
    addStudent(name)

    while True:
        rta = input('¿Desea ingresar otro aspirante? S(si) o Enter(No)')
        if rta in rtas:
            break
        elif rta not in rtas and rta != '':
            print('Respuesta no valida, intente nuevamente')
        elif bool(rta) == False :
            isAddStudent = False
            break
print(aspirantes)


"""
Llevar el control academico de los estudiantes, donde tendra un menu principal con las siguientes opciones:
Registro y Control academico
1. Registrar Estudiante
2. Registro de Calificaciones
    Registro de Notas
    1. Registrar Nota Proyecto
    2. Registrar Nota Examen
    3. Registrar Nota Actividad
    0. Volver al menu principal
3. Estadisticas
    Estadisticas
    1. Listar Notas de un Estudiante - Debo ingresar nombre estudiante y buscar en la lista y mostrar las notas
    2. Mostrar el Promedio Academico del Grupo
    3. Listar los Estudiantes que Perdieron el Skill
    4. Listar Estudiantes con una Calificacion Alta
    0. Volver al menu principal
0. Salir

NOTAS:
PROYECTO = 60%
EXAMEN = 25%
ACTIVIDAD = 15%

SE PIERDE SKILL CON UNA NOTA INFERIOR A 65
SE CONSIDERA CALIFICACION ALTA > 85
"""
