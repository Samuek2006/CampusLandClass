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

#Funcion de limpiar la consola
def LimpiarConsola():
    limpiar = os.system('cls' if os.name == 'nt' else 'clear')
    return limpiar

#Funcion add Student
def addStudent(name : str):
    student.append([name, [], [], []])
    print(Fore.CYAN + f'El estudiante {name} ha sido agregado con exito')
    input(Fore.MAGENTA + 'Enter para continuar')

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
                pass

            case 0:
                pass

            case _:
                print('Opcion Invalida Intentelo Nuevamente...')
                time.sleep(1)

    except (ValueError, KeyboardInterrupt, TypeError, IndexError, UnboundLocalError) as e:
        print(f'Error: {e}')

