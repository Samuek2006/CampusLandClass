from modules.util import login as login
from modules.util import utilidades as util


def EstadoCamper():
    while True:
        try:
            print('''
1. Inscrito
2. Aprobado
3. Cursando
4. Graduado
5. Expulsado
6. Retirado
            ''')
            estado = int(input('Ingresa una Opcion: '))
            if estado in range(1, 7):

                return estado
            else:
                print("⚠️ Debes ingresar un número entre 1 y 6.")

        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú.")
            return None
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú.")
            return None


def menuRutasAprendizaje():
    while True:
        try:
            print('''
1. Fundamentos de Programacion (Introducción a la algoritmia, PSeInt y Python)
2. Programacion Web (HTML, CSS y Bootstrap)
3. Programacion Formal (Java, JavaScript, C#)
4. Bases de datos (Mysql, MongoDb y Postgresql). Cada ruta tiene un SGDB principal y un alternativo
5. Backend (NetCore, Spring Boot, NodeJS y Express)
            ''')
            opcion = int(input('Ingresa una Opcion: '))
            if opcion in range(1, 6):
                return opcion

            else:
                print("⚠️ Opción fuera de rango. Debe estar entre 1 y 5.")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú.")
            return None
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú.")
            return None


def menuPrincipal():
    while True:
        try:
            util.Limpiar_consola()
            opcion = input('Ya te registraste (S/N): ').strip().upper()

            match opcion:
                case "S":
                    util.Limpiar_consola()
                    print('=== Registrate aqui ===')
                    util.Stop()
                    util.Limpiar_consola()

                    login.register()
                    util.Stop()
                    util.Limpiar_consola()

                case "N":
                    util.Limpiar_consola()
                    print('=== Logeate aqui ===')
                    util.Stop()
                    util.Limpiar_consola()

                    login.login()
                    util.Stop()
                    util.Limpiar_consola()

                case _:
                    util.Limpiar_consola()
                    print('⚠️ Ingresa una opción válida (S/N)')
                    util.Stop()
                    util.Limpiar_consola()

        except ValueError:
            print("❌ Error: Ingresa una Opcion Valida.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

def menuCoordinador():
    while True:
        try:
            util.Limpiar_consola()

            print("""
=== MENU COORDINADOR ===
1. Gestión de Campers
2. Admisiones
3. Gestión de Trainers
4. Gestión de Rutas
5. Gestión de Áreas/Salones
6. Matrículas
7. Reportes
0. Salir
            """)
            opcion = int(input('Ingresa una Opcion: '))

            match opcion:
                case 1:
                    pass

                case 2:
                    pass

                case 3:
                    pass

                case 4:
                    pass

                case 5:
                    pass

                case 6:
                    pass

                case 7:
                    pass

                case 0:
                    print('Saliendo...')
                    break

                case _:
                    util.Limpiar_consola()
                    print("⚠️ Opción fuera de rango. Debe estar entre 1 y 7.")
                    util.Stop()
                    util.Limpiar_consola()

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

def menuTrainer():
    while True:
        try:
            util.Limpiar_consola()

            print(""""
1. Mi información
2. Campers asignados
3. Registrar notas por módulo
4. Ver resultados de mis campers
0. Salir
                """)
            opcion = int(input('Ingresa una Opcion: '))

            match opcion:
                case 1:
                    pass

                case 2:
                    pass

                case 3:
                    pass

                case 4:
                    pass

                case 0:
                    print('Saliendo...')
                    util.Stop()
                    util.Limpiar_consola()

                case _:
                    util.Limpiar_consola()
                    print("⚠️ Opción fuera de rango. Debe estar entre 1 y 4.")
                    util.Stop()
                    util.Limpiar_consola()

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

def menuCamper():
    while True:
        try:
            util.Limpiar_consola()

            print(""""
1. Mi información
2. Mi matrícula
3. Mi progreso
0. Salir
                """)
            opcion = int(input('Ingresa una Opcion: '))

            match opcion:
                case 1:
                    pass

                case 2:
                    pass

                case 3:
                    pass

                case 0:
                    print('Saliendo...')
                    util.Stop()
                    util.Limpiar_consola()

                case _:
                    util.Limpiar_consola()
                    print("⚠️ Opción fuera de rango. Debe estar entre 1 y 3.")
                    util.Stop()
                    util.Limpiar_consola()

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break