import util.corefiles as corefiles
import util.utilidades as util
from modules.coordinadorAcademico import admin as admin

DB_KnowledgeLand = 'data/KnowledgeLand.json'

corefiles.initialize_json(DB_KnowledgeLand, {
    'Estudiantes': {},
    'Bibliotecario': {},
    'CoordinadorAcademico': {}
})

def menuPrincipal():
    while True:
        try:
            print('''
1. Estudiante
2. Bibliotecario
3. Coordinador Academico
0. Salir
''')
            opcion = int(input('Ingresa una Opcion: '))

            match opcion:
                case 1:
                    util.limpiarConsola()
                    menuEstudiante()
                    util.stop()

                case 2:
                    util.limpiarConsola()
                    menuBibliotecario()
                    util.stop()
                    util.limpiarConsola()

                case 3:
                    util.limpiarConsola()
                    menuCoordinador()
                    util.stop()
                    util.limpiarConsola()

                case 0:
                    util.limpiarConsola()
                    print('Saliendo...')
                    util.stop()
                    util.limpiarConsola()
                    break

                case _:
                    util.limpiarConsola()
                    print('Ingresa una Opcion valida (0 - 3)')
                    util.stop()
                    util.limpiarConsola()

        except TypeError:
            print('Error de Type de dato')
            return None
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")
            return None
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú.")
            return None
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú.")
            return None

def menuEstudiante():
    while True:
        try:
            print('''
1. Consultar catálogo de libros
2. Reservar libro
3. Prestar libro
4. Devolver libro
5. Estado de cuenta
0. Volver al menú principal
''')
            opcion = int(input('Ingresa una Opcion: '))

            match opcion:
                case 1:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 2:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 3:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 4:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 5:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 0:
                    util.limpiarConsola()
                    print('Regresando...')
                    util.stop()
                    util.limpiarConsola()
                    break

                case _:
                    util.limpiarConsola()
                    print('Ingresa una Opcion Valida (0 - 5)')
                    util.stop()
                    util.limpiarConsola()

        except TypeError:
            print('Error de Type de dato')
            return None
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")
            return None
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú.")
            return None
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú.")
            return None

def menuBibliotecario():
    while True:
        try:
            print('''
1. Registrar nuevo libro
2. Actualizar stock de libros
3. Registrar devolución y sanciones
4. Cambiar estado de estudiante
0. Volver al menú principal
''')
            opcion = int(input('Ingresa una Opcion: '))

            match opcion:
                case 1:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 2:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 3:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 4:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 0:
                    util.limpiarConsola()
                    print('Regresando...')
                    util.stop()
                    util.limpiarConsola()
                    break

                case _:
                    util.limpiarConsola()
                    print('Ingresa una Opcion Valida (0 - 5)')
                    util.stop()
                    util.limpiarConsola()

        except TypeError:
            print('Error de Type de dato')
            return None
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")
            return None
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú.")
            return None
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú.")
            return None

def menuCoordinador():
    while True:
        try:
            print('''
1. Agregar Usuarios
2. Estudiantes sancionados
3. Libros más prestados
4. Préstamos activos
5. Estadísticas de uso
0. Volver al menú principal
''')
            opcion = int(input('Ingresa una Opcion: '))

            match opcion:
                case 1:
                    util.limpiarConsola()
                    subAgregarUsuario()
                    util.stop()
                    util.limpiarConsola()

                case 2:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 3:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 4:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 5:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 0:
                    util.limpiarConsola()
                    print('Regresando...')
                    util.stop()
                    util.limpiarConsola()
                    break

                case _:
                    util.limpiarConsola()
                    print('Ingreas una Opcion Valida (0 - 4)')
                    util.stop()
                    util.limpiarConsola()

        except TypeError:
            print('Error de Type de dato')
            return None
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")
            return None
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú.")
            return None
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú.")
            return None

def subAgregarUsuario():
    while True:
        try:
            print('''
1. Agregar Estudiante
2. Agregar Bibliotecario
3. Agregar Coordinador Academico
0. Volver al menu principal
''')
            opcion = int(input('Ingresa una Opcion: '))

            match opcion:
                case 1:
                    util.limpiarConsola()
                    print('=== Agregar Estudiante ===')
                    admin.addStudent()
                    input('Enter Para Continuar...')
                    util.stop()
                    util.limpiarConsola()

                case 2:
                    util.limpiarConsola()
                    print('=== Agregar Bibliotecario ===')
                    admin.addLibrarian()
                    input('Enter Para Continuar...')
                    util.stop()
                    util.limpiarConsola()

                case 3:
                    util.limpiarConsola()
                    print('=== Agregar Coordinador Academico ===')
                    admin.addAcademicCoordinator()
                    input('Enter Para Continuar...')
                    util.stop()
                    util.limpiarConsola()

                case 0:
                    util.limpiarConsola()
                    print('Regresando...')
                    util.stop()
                    util.limpiarConsola()
                    break

                case _:
                    util.limpiarConsola()
                    print('Ingreas una Opcion Valida (0 - 3)')
                    util.stop()
                    util.limpiarConsola()

        except TypeError:
            print('Error de Type de dato')
            return None
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")
            return None
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú.")
            return None
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú.")

def subEstadisticas():
    while True:
        try:

            print('''
1. total préstamos
2. devoluciones
3. reservas
0. Volver al menú Coordinador
''')
            opcion = int(input('Ingresa una Opcion: '))

            match opcion:
                case 1:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 2:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 3:
                    util.limpiarConsola()
                    util.stop()
                    util.limpiarConsola()

                case 0:
                    util.limpiarConsola()
                    print('Regresando...')
                    util.stop()
                    util.limpiarConsola()
                    break

                case _:
                    util.limpiarConsola()
                    print('Ingreas una Opcion Valida (0 - 3)')
                    util.stop()
                    util.limpiarConsola()

        except TypeError:
            print('Error de Type de dato')
            return None
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")
            return None
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú.")
            return None
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú.")