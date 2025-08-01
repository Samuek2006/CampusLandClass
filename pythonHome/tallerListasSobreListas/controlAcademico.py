"""
Autor: Samuel Felipe Calderón Soto
Fecha: 31/07/2025
Descripcion: Este Script es un control academico
"""
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

"""
Autor: Samuel Felipe Calderón Soto
Fecha: 31/07/2025
Descripcion: Este Script es un control academico
"""

import os, time
from colorama import Fore, Style, init
init(autoreset=True)

db = []
rtas = ['S', 's']

#Funcion para limpiar de la consola
def LimpiarConsola():
    limpiar = os.system('cls')
    return limpiar

#Funcion para registrar estudiantes
def addStudent(name : str):
    db.append([name, [], [], []])
    print(Fore.GREEN + f'Student {name} agregado Exitosamente.')
    input(Fore.BLUE + 'Presione Enter para continuar...')

#Funcion que me carga dinamicamente el menu de Estadisticas
def Estadisticas():
    opcionEstadisticas = int(input(
        Fore.CYAN + 'ESTADISTICAS\n' +
        Fore.YELLOW + '1. Listar Notas de un Estudiante\n' +
        '2. Mostrar el Promedio Academico del Grupo\n' +
        '3. Listar los Estudiantes que Perdieron el Skill\n' +
        '4. Listar Estudiantes con una Calificacion Alta\n' +
        '0. Volver al menu principal\n' +
        Fore.MAGENTA + 'Ingresa tu Opcion: '
    ))
    return opcionEstadisticas

#Funcion que me carga dinamicamente el menu de Registro de Notas
def RegistroNotas():
    opcionRegistro = int(input(
        Fore.CYAN + 'REGISTRO DE NOTAS\n' +
        Fore.YELLOW + '1. Registrar Nota Proyecto\n' +
        '2. Registrar Nota de Examenes\n' +
        '3. Registrar Nota de Actividad\n' +
        '0. Volver al menu principal\n' +
        Fore.MAGENTA + 'Ingresa tu opcion: '
    ))
    return opcionRegistro

#Funcion que me carga dinamicamente el Menu Principal
def MenuControlAcademico():
    opcionControl = int(input(
        Fore.CYAN + 'REGISTRO Y CONTROL ACADEMICO\n' +
        Fore.YELLOW + '1. Registrar Estudiante\n' +
        '2. Registro de Calificaciones\n' +
        '3. Estadisticas\n' +
        '0. Salir\n' +
        Fore.MAGENTA + 'Ingresa tu opcion: '
    ))
    return opcionControl

#Funcion para formatear como se imprimen los datos de las notas
def formatearNotas(lista):
    return ', '.join(map(str, lista)) if lista else 'Sin notas registradas'

#Funcion para saber el promedio de cada estudiante en el skill
def promedioEstudiante(estudiante):
    notasProyecto = estudiante[1]
    notasExamenes = estudiante[2]
    notasActividades = estudiante[3]

    promedioProyecto = sum(notasProyecto) / len(notasProyecto) if notasProyecto else 0
    promedioExamen = sum(notasExamenes) / len(notasExamenes) if notasExamenes else 0
    promedioActividad = sum(notasActividades) / len(notasActividades) if notasActividades else 0

    promedioGeneral = (promedioProyecto * 0.6) + (promedioExamen * 0.25) + (promedioActividad * 0.15)
    return promedioGeneral

#Funcion para la carga dinamica
def Cargando():
    progreso = 10
    LimpiarConsola()
    for i in range(progreso + 1):
        barra = '- ' * i
        porcentaje = (i * 10)
        texto = f'{Fore.RED}({barra:<20}) {porcentaje} / 100'
        print(texto.ljust(40), end='\r')  # .ljust rellena con espacios
        time.sleep(0.1)
    print()  # Salto de línea final
    time.sleep(0.5)
    LimpiarConsola()

while True:
    try:
        Cargando()
        opcion = MenuControlAcademico()
        match opcion:
            case 1:
                Cargando()
                LimpiarConsola()
                print(Fore.BLUE + 'Registro de Estudiante')
                nameStudent = input(Fore.YELLOW + 'Ingresa el Nombre del Estudiante: ')
                addStudent(nameStudent)

            case 2:
                while True:
                    try:
                        LimpiarConsola()
                        Cargando()
                        opcionRegistro = RegistroNotas()
                        match opcionRegistro:
                            case 1:
                                LimpiarConsola()
                                Cargando()
                                nombreEstudianteNota = input(Fore.YELLOW + 'Ingresa el nombre del estudiante: ')
                                encontrado = False
                                for estudiante in db:
                                    if estudiante[0] == nombreEstudianteNota:
                                        notaEstudiante = int(input(Fore.YELLOW + 'Ingresa la nota de Proyecto del estudiante: '))
                                        estudiante[1].append(notaEstudiante)
                                        print(Fore.GREEN + f'Nota {notaEstudiante} registrada para {nombreEstudianteNota}')
                                        encontrado = True
                                        break
                                if not encontrado:
                                    print(Fore.RED + f'El estudiante {nombreEstudianteNota} no esta registrado.')
                                input(Fore.BLUE + 'Presione Enter para Continuar...')

                            case 2:
                                LimpiarConsola()
                                Cargando()
                                nombreEstudianteNota = input(Fore.YELLOW + 'Ingresa el nombre del estudiante: ')

                                encontrado = False
                                for estudiante in db:
                                    if estudiante[0] == nombreEstudianteNota:
                                        notaEstudiante = int(input(Fore.YELLOW + 'Ingresa la nota de Extamen del estudiante: '))
                                        estudiante[2].append(notaEstudiante)
                                        print(Fore.GREEN + f'Nota {notaEstudiante} registrada para {nombreEstudianteNota}')
                                        encontrado = True
                                        break
                                if not encontrado:
                                    print(Fore.RED + f'El estudiante {nombreEstudianteNota} no esta registrado.')
                                input(Fore.BLUE + 'Presione Enter para Continuar...')

                            case 3:
                                LimpiarConsola()
                                Cargando()
                                nombreEstudianteNota = input(Fore.YELLOW + 'Ingresa el nombre del estudiante: ')

                                encontrado = False
                                for estudiante in db:
                                    if estudiante[0] == nombreEstudianteNota:
                                        notaEstudiante = int(input(Fore.YELLOW + 'Ingresa la nota de Actividades del estudiante: '))
                                        estudiante[3].append(notaEstudiante)
                                        print(Fore.GREEN + f'Nota {notaEstudiante} registrada para {nombreEstudianteNota}')
                                        encontrado = True
                                        break
                                if not encontrado:
                                    print(Fore.RED + f'El estudiante {nombreEstudianteNota} no esta registrado.')
                            case 0:
                                break
                            case _:
                                print(Fore.RED + 'Opcion Invalida')
                    except (ValueError, KeyboardInterrupt, AttributeError) as e:
                        print(Fore.RED + f'Error: {e}')


            case 3:
                while True:
                    try:
                        LimpiarConsola()
                        Cargando()
                        opcionEstadisticas = Estadisticas()
                        match opcionEstadisticas:
                            case 1:
                                LimpiarConsola()
                                Cargando()
                                nombreEstudianteNota = input(Fore.YELLOW + 'Ingresa el nombre del estudiante: ')
                                encontrado = False
                                for estudiante in db:
                                    if estudiante[0] == nombreEstudianteNota:
                                        print(Fore.MAGENTA + f'El estudiante: {nombreEstudianteNota} Tiene las siguientes notas:\n' +
                                                f'- Nota Proyecto: {formatearNotas(estudiante[1])}\n' +
                                                f'- Nota de Examenes: {formatearNotas(estudiante[2])}\n' +
                                                f'- Nota de Actividades: {formatearNotas(estudiante[3])}')
                                        encontrado = True
                                        break
                                if not encontrado:
                                    print(Fore.RED + f'El estudiante {nombreEstudianteNota} no esta registrado.')
                                input(Fore.BLUE + 'Presione Enter para Continuar...')

                            case 2:
                                LimpiarConsola()
                                Cargando()
                                print(Fore.BLUE + 'Promedio de Notas de los Estudiantes del Grupo')
                                if not db:
                                    print(Fore.RED + 'No hay Estudiantes Registrados')
                                else:
                                    suma_promedios = 0
                                    for estudiante in db:
                                        suma_promedios += promedioEstudiante(estudiante)
                                    promedio_grupal = suma_promedios / len(db)

                                    print(Fore.MAGENTA + f"Promedio general del grupo: {promedio_grupal:.2f}\n")
                                    print(Fore.MAGENTA + "Promedio individual por estudiante:")
                                    for estudiante in db:
                                        nombre = estudiante[0]
                                        promedio = promedioEstudiante(estudiante)
                                        print(Fore.YELLOW + f'{nombre}: {promedio:.2f}')
                                input(Fore.BLUE + '\nPresione Enter para Continuar...')


                            case 3:
                                LimpiarConsola()
                                Cargando()
                                print(Fore.BLUE + 'Lista Estudiantes que Perdieron el Skill')
                                perdedores = [(e[0], promedioEstudiante(e)) for e in db if promedioEstudiante(e) < 65]

                                if perdedores:
                                    for nombre, promedio in perdedores:
                                        print(Fore.RED + f'{nombre}: {promedio:.2f}')
                                else:
                                    print(Fore.GREEN + 'Ningun Estudiante perdio el Skill')

                                input(Fore.BLUE + 'Presione Enter para Continuar...')

                            case 4:
                                LimpiarConsola()
                                Cargando()
                                print(Fore.BLUE + 'Lista Estudiantes con una Calificacion Alta')
                                destacados = [(e[0], promedioEstudiante(e)) for e in db if promedioEstudiante(e) > 85]

                                if destacados:
                                    for nombre, promedio in destacados:
                                        print(Fore.GREEN + f'{nombre}: {promedio:.2f}')
                                else:
                                    print(Fore.YELLOW + 'Ningún estudiante tiene calificación alta')

                                input(Fore.BLUE + 'Presione Enter para Continuar...')

                            case 0:
                                break
                            case _:
                                print(Fore.RED + 'Opcion Invalida')
                    except (ValueError, KeyboardInterrupt, AttributeError) as e:
                        print(Fore.RED + f'Error: {e}')

            case 0:
                Cargando()
                eleccion = input(Fore.YELLOW + 'Deseas salir del Sistema?  (S/N): ').upper()
                if eleccion == 'S':
                    print(Fore.GREEN + 'Gracias por Usar Nuestro Sistema, Vuelva Pronto')
                    time.sleep(2)
                    LimpiarConsola()
                    print(Fore.MAGENTA + "Cerrando El Sistema...")
                    time.sleep(0.5)
                    LimpiarConsola()
                    break
                else:
                    print(Fore.RED + 'Opcion Invalidad')
                    time.sleep(1)
            case _:
                print(Fore.RED + 'Opcion Invalida')
    except (ValueError, KeyboardInterrupt, AttributeError) as e:
        print(Fore.RED + f'Error: {e}')
