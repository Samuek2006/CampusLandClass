"""
Se necesita realizar un algoritmo que permita a un profesor de matematicas calcular la nota final de los estudiantes de su grupo de matematicas discretas, Teniendo en cuenta los siguientes requerimientos:

    - El grupo esta conformado por 10 estudiantes
    - La notas estan Divididas en parciales, quices y Trabajos, Los parciales tienen un valor de 60% de la asignatura, los Quices tienen un valor del 25% y los trabajos tienen un valor del 15%.
    - El programa debe mostrar el siguiente resumen academico:
        - Promedio general del grupo
        - Total de estudiantes que aprobaron la asignatura
        - Total de estudiantes que reprobaron la asignatura
        - Total de estudiantes que obtuvieron una nota entre 1 y 2.9
        - Total de estudiantes que obtuvieron una nota entre 3 y 3.5
        - Nota mas alta del grupo
        - Nota mas baja del grupo
        - Total de estudiantes que obtuvieron una nota superior al promedio general

"""

import os, time
from colorama import Fore, Style, init
init(autoreset=True)

#Variables
student = []

#contadores
aprobaron = 0
reprobaron = 0
NotaPerdida = 0
notaRegular = 0

#Funcion de limpiar la consola
def LimpiarConsola():
    limpiar = os.system('cls' if os.name == 'nt' else 'clear')
    return limpiar

#Funcion add Student
def addStudent(name : str):
    student.append([name, [], [], []])
    print(Fore.CYAN + f'El estudiante {name} ha sido agregado con exito')
    input(Fore.MAGENTA + 'Enter para continuar')

def FormatearNotas(lista):
    return ', '.join(map(str, lista)) if lista else 'No hay notas'

def promedioEstudiante(student):
    notasProyecto = estudiante[1]
    notasExamenes = estudiante[2]
    notasActividades = estudiante[3]

    promedioProyecto = sum(notasProyecto) / len(notasProyecto) if notasProyecto else 0
    promedioExamen = sum(notasExamenes) / len(notasExamenes) if notasExamenes else 0
    promedioActividad = sum(notasActividades) / len(notasActividades) if notasActividades else 0

    promedioGeneral = (promedioProyecto * 0.6) + (promedioExamen * 0.25) + (promedioActividad * 0.15)
    if promedioGeneral >= 65:
        aprobaron += 1
    else:
        reprobaron += 1
    return promedioGeneral

def NotaPerdida(nota):
    if nota < 65:
        NotaPerdida += 1
    elif nota >= 65 and nota <= 75:
        notaRegular += 1
    else:
        print('Nota fuera de rango')

#Ejecucion Principal
while True:
    try:
        LimpiarConsola()
        opcion = int(input(Fore.CYAN + 'Matematicas Discretas' + Fore.YELLOW + '\n1. Agregar Estudiante \n2. Registrar Notas \n3. Estadisticas \n0. Salir' + Fore.MAGENTA +  '\nIngrese una opcion: '))

        match opcion:
            case 1:
                LimpiarConsola()
                print(Fore.CYAN + 'Registras Estudiante')
                name = input(Fore.MAGENTA + 'Ingrese el nombre del estudiante: ')
                addStudent(name)
                time.sleep(1)
                LimpiarConsola()

            case 2:
                LimpiarConsola()
                while True:
                    try:
                        print(Fore.CYAN + 'Registrar Notas Estudiantes')
                        opcion = int(input(Fore.YELLOW + '\n1. Registrar nota del parciales \n2. Registrar nota de los quices \n3. Registrar nota de los Trabajos \n0. Salir' + Fore.MAGENTA + '\nIngresa una opcion: '))

                        match opcion:
                            case 1:
                                name = input(Fore.MAGENTA + 'Ingrese el nombre del estudiante: ')
                                encontrado = False
                                LimpiarConsola()

                                print(Fore.RED + 'Buscando Estudiante...')
                                time.sleep(0.5)
                                LimpiarConsola()

                                for estudiante in student:
                                    if estudiante[0] == name:

                                        print(Fore.RED + f'Estudiante {name} encontrado')
                                        time.sleep(0.5)
                                        LimpiarConsola()

                                        notaParcial = int(input(Fore.MAGENTA + 'Ingrese las notas del parcial: '))
                                        estudiante[1].append(notaParcial)
                                        print(Fore.CYAN + f'Nota del parcial {notaParcial} agregada correctamente al estudiante: {name}')
                                        time.sleep(1)
                                        NotaPerdida(notaParcial)
                                        encontrado = True
                                        LimpiarConsola()
                                        break

                                    else:
                                        print(Fore.RED + f'Estudiante {name} no encontrado')
                                        time.sleep(0.5)
                                        LimpiarConsola()

                            case 2:
                                name = input(Fore.MAGENTA + 'Ingrese el nombre del estudiante: ')
                                encontrado = False
                                LimpiarConsola()

                                print(Fore.RED + 'Buscando Estudiante...')
                                time.sleep(0.5)
                                LimpiarConsola()

                                for estudiante in student:
                                    if estudiante[0] == name:

                                        print(Fore.RED + f'Estudiante {name} encontrado')
                                        time.sleep(0.5)
                                        LimpiarConsola()

                                        notaQuiz = int(input(Fore.MAGENTA + 'Ingrese las notas del Quiz: '))
                                        estudiante[2].append(notaQuiz)
                                        print(Fore.CYAN + f'Nota del parcial {notaQuiz} agregada correctamente al estudiante: {name}')
                                        time.sleep(1)
                                        NotaPerdida(notaQuiz)
                                        encontrado = True
                                        LimpiarConsola()
                                        break

                                    else:
                                        print(Fore.RED + f'Estudiante {name} no encontrado')
                                        time.sleep(0.5)
                                        LimpiarConsola()


                            case 3:
                                name = input(Fore.MAGENTA + 'Ingrese el nombre del estudiante: ')
                                encontrado = False
                                LimpiarConsola()

                                print(Fore.RED + 'Buscando Estudiante...')
                                time.sleep(0.5)
                                LimpiarConsola()

                                for estudiante in student:
                                    if estudiante[0] == name:

                                        print(Fore.RED + f'Estudiante {name} encontrado')
                                        time.sleep(0.5)
                                        LimpiarConsola()

                                        notaTaller = int(input(Fore.MAGENTA + 'Ingrese las notas del Taller: '))
                                        estudiante[3].append(notaTaller)
                                        print(Fore.CYAN + f'Nota del parcial {notaTaller} agregada correctamente al estudiante: {name}')
                                        time.sleep(1)
                                        NotaPerdida(notaTaller)
                                        encontrado = True
                                        LimpiarConsola()
                                        break

                                    else:
                                        print(Fore.RED + f'Estudiante {name} no encontrado')
                                        time.sleep(0.5)
                                        LimpiarConsola()

                            case 0:
                                LimpiarConsola()
                                print(Fore.RED + 'Volviendo al menu principal...')
                                time.sleep(0.5)

                            case _:
                                pass

                    except (ValueError, KeyboardInterrupt, TypeError, IndexError, UnboundLocalError) as e:
                        print(f'Error: {e}')

            case 3:
                print(Fore.CYAN + 'Estadisticas' )
                opcion = int(input(Fore.YELLOW + '\n1. Promedio General del Grupo \n2. Total de Estudiantes que Aprovaron la Asignatura \n3. Total de Estudiantes que Reprovaron la Asignatura \n4. Total de Estudiantes que Obtuvieron una Nota entre 1 y 2.9 \n5. Total de Estudiantes que Obtuvieron una Nota entre 3 y 3.5 \n6. Nota mas Alta del Grupo \n7. Nota mas Baja del Grupo \n8. Total de Estudiantes que Obtuvieron una Nota Superior al Promedio \n0. Salir' + Fore.MAGENTA + '\nIngresa una Opcion: '))

                match opcion:
                    case 1:
                        LimpiarConsola()
                        print('Promedio de Notas de los Estudiante del Grupo')

                        if not student:
                            print('No hay estudiantes en el grupo')
                        else:
                            sumaPromedios = 0
                            for estudiante in student:
                                sumaPromedios += promedioEstudiante(estudiante)
                            promedioGrupal = sumaPromedios / len(student)

                            print(Fore.CYAN + f'Promedio general del grupo: {promedioGrupal:.2f}')
                            print(Fore.CYAN + 'Promedio individual por estudiante: ')
                            for estudiante in student:
                                nombre = estudiante[0]
                                promedio = promedioEstudiante(estudiante)
                                print(Fore.YELLOW + f'{nombre}: {promedio:.2f}')
                        input(Fore.MAGENTA + 'Enter para Continuar...')

                    case 2:
                        LimpiarConsola()
                        print('Total de Estudiantes que Aprovaron la Asignatura')
                        print(f'Aprovados: {aprobaron}')

                    case 3:
                        LimpiarConsola()
                        print('Total de Estudiantes que Reprovaron la Asignatura')
                        print(f'Aprovados: {reprobaron}')

                    case 4:
                        print('Total de Estudiantes que Obtuvieron una Nota menor a 65')
                        print(f'Total Estudiantes: {NotaPerdida}')

                    case 5:
                        print('Total de Estudiantes que Obtuvieron una Nota entre 65 y 75')
                        print(f'Total Estudiantes: {notaRegular}')

            case 0:
                pass

            case _:
                print('Opcion Invalida Intentelo Nuevamente...')
                time.sleep(1)

    except (ValueError, KeyboardInterrupt, TypeError, IndexError, UnboundLocalError) as e:
        print(f'Error: {e}')

