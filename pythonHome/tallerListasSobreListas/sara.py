import os

dataBase = []
rta = ['S', 's']

def AgregarEstudiantes(nombre : str):
    dataBase.append([nombre, [], [], []])
    print(f'Estudiante {nombre} registrado exitosamente')

#menu de estadisticas
def MenuEstadisticas():
    opcionEstadisticas = int(input('Estadisticas \n1. Listas de notas estudiantes \n2. Mostrar promedio academico del grupo \n3. Listar estudiantes que perdieron el skill \n4. Listar estudiantes con calificacion alta \n5. Salir del menu'))
    return opcionEstadisticas

#menu de registro de notas 
def MenuRegistro():
    opcionRegistro = int(input('Registro \n1. Registrar nota proyecto \n2. registrar nota de examenes \n3. Registrar nota de actividad \n4. Salir del menu'))
    return opcionRegistro

#menu principal
def MenuPrincipal():
    opcionControl = int(input('Control \n1. Registrar estudiantes \n2. Registro de calificaciones \n3. estadisticas \n4. salir'))
    return opcionControl

#formatear variables
def FormatearVariables(lista):
    return ', '.join(map(str, lista)) if lista else 'No tiene notas registradas'

def PromedioEstudiantes(estudiante):
    notaProyecto = estudiante[1]
    notaExamenes = estudiante[2]
    notaActividad = estudiante[3]

    promedioProyectos = sum(notaProyecto) / len(notaProyecto) if notaProyecto else 0
    promedioExamenes = sum(notaExamenes) / len(notaExamenes) if notaExamenes else 0
    promedioActividad = sum(notaActividad) / len(notaActividad) if notaActividad else 0

    promedioGeneral = (promedioProyectos * 0.6) + (promedioExamenes * 0.25) + (promedioActividad * 0.15)
    return promedioGeneral

#Ejecucion
while True:
    try:
        opcionMenu = MenuPrincipal()
        match opcionMenu:
            case 1: 
                print('Registro Estudiantes')
                nombreEstudiante = input('Ingresa el nombre del estudiante: ')
                AgregarEstudiantes(nombreEstudiante)
                input('Enter para continuar...')
            case 2: 
                opcionRegistro = MenuRegistro()
                match opcionRegistro:
                    case 1:
                        print('Registro Calificaciones')
                        nombreEstudiante = input('Ingresa el nombre del estudiante: ')
                        notaProyecto = float(input('Ingresa la nota del proyecto: '))
                        encontrado = False

                        for estudiante in dataBase:
                            if estudiante[0] == nombreEstudiante:
                                estudiante[1].append(notaProyecto)
                                print(f'Nota del proyecto de {nombreEstudiante} registrada exitosamente')
                                encontrado = True
                                break
                            else:
                                print('Estudiante no encontrado')
                        if not encontrado:
                            print(f'El estudiante {nombreEstudiante} no existe')
                        input('Presione enter para continuar...')
                    case 2:
                        nombreEstudiante = input('Ingresa el nombre del estudiante: ')
                        notaExamen = float(input('Ingresa la nota del examen: '))
                        encontrado = False

                        for estudiante in dataBase:
                            if estudiante[0] == nombreEstudiante:
                                estudiante[2].append(notaExamen)
                                print(f'Nota del examen de {nombreEstudiante} registrada exitosamente')
                                encontrado = True
                                break
                            else:
                                print('Estudiante no encontrado')
                        if not encontrado:
                            print(f'El estudiante {nombreEstudiante} no existe')
                        input('Presione enter para continuar...')
                    case 3:
                        nombreEstudiante = input('Ingresa el nombre del estudiante: ')
                        notaActividad = float(input('Ingresa la nota de la actividad: '))
                        encontrado = False

                        for estudiante in dataBase:
                            if estudiante[0] == nombreEstudiante:
                                estudiante[3].append(notaActividad)
                                print(f'Nota de la actividad de {nombreEstudiante} registrada exitosamente')
                                encontrado = True
                                break
                            else:
                                print('Estudiante no encontrado')
                        if not encontrado:
                            print(f'El estudiante {nombreEstudiante} no existe')
                        input('Presione enter para continuar...')
                    case 4:
                        print('volviendo al menu principal')
                        break
                    case _:
                        print('Opcion invalida')
            case 3: 
                opcionEstadisticas = MenuEstadisticas()
                match opcionEstadisticas:
                    case 1:
                        nombreEstudiante = input('Ingresa el nombre del estudiante: ')
                        encontrado = False
                        for estudiante in dataBase:
                            if estudiante[0] == nombreEstudiante:
                                print(f'El estudiante {nombreEstudiante} Tiene las siguientes notas: \n- nota proyecto: {estudiante[1]} \n- nota examen: {estudiante[2]} \n- nota actividad: {estudiante[3]}')
                                encontrado = True
                                break
                        if not encontrado:
                            print(f'El estudiante {nombreEstudiante} no existe')
                        input('Presione Enter para continuar...')
                    case 2:
                        print('Promedio Notas de los estudiantes del grupo')
                        if not dataBase:
                            print('No hay estudiantes Registrados')
                        else:
                            notaPro = 0
                            notaExan = 0
                            notaActi = 0
                            count = 0
                            print('Promedio academico del grupo:')
                            for estudiantes in dataBase:
                                nombre = estudiantes[0]
                                promedio = PromedioEstudiantes(estudiante)
                                if promedio > 0:
                                    print(f'El estudiante {nombre} tiene un promedio de {promedio}')
                                    notaPro += sum(estudiante[1])
                                    notaExan += sum(estudiante[2])
                                    notaActi += sum(estudiante[3])
                                    count += 1
                            if count > 0:
                                promedioGrupo = ((notaPro * 0.6) + (notaExan * 0.25) + (notaActi * 0.15))/count
                            else:
                                print('no hay estudiantes con notas')
                        input('Enter para continuar')
                    case 3:
                        print('Lista de estudiantes que perdieron el skill')
                        perdedores = []
                        for estudiantes in dataBase:
                            promedio = PromedioEstudiantes(estudiantes)
                            if promedio < 65:
                                perdedores.append((estudiantes[0], promedio))
                        if perdedores:
                            for nombre, promedio in perdedores:
                                print(f'El estudiante {nombre} perdió el skill con un promedio de {promedio}')
                            else:
                                print('No hay estudiantes que perdieron el skill')
                        input('Enter para continuar')
                    case 4:
                        destacados = []
                        for estudiante in dataBase:
                            promedio = PromedioEstudiantes(estudiante)
                            if promedio > 85:
                                destacados.append((estudiante[0], promedio))

                        if destacados:
                            for nombre, promedio in destacados:
                                print(f'{nombre}: {promedio:.2f}')
                        else:
                            print('Ningún estudiante tiene calificación alta')

                        input('Presione Enter para Continuar...')
                    case 0:
                        print('volviendo al menu principal')
                        break
                    case _:
                        print('Opcion invalida')
            case 4: 
                print('saliendo del programa')
                break
            case _: 
                print('Opcion invalida')
    except (ValueError, KeyboardInterrupt) as e:
        print(f'Error: {e}')

