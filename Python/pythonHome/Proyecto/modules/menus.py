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
                case "N":
                    util.Limpiar_consola()
                    print('=== Registrate aqui ===')
                    util.Stop()
                    util.Limpiar_consola()

                    login.register()
                    util.Stop()
                    util.Limpiar_consola()

                case "S":
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

"""
Sub Menus del Coordinador
"""
def SubGestionCampers():
    while True:
        try:
            print("""
=== Gestion De Campers ===
1. Registrar Camper
2. Listar campers
3. Consultar camper individual
4. Cambiar estado
5. Marcar/consultar riesgo
0. Salir
""")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

def SubAdmisiones():
    while True:
        try:
            print("""
=== Admisiones ===
1. Registrar notas de examen de ingreso
2. Calcular promedio ⇒ actualizar estado
3. Listar aprobados examen.
0. Salir
""")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

def SubGestionTrainer():
    while True:
        try:
            print("""
=== Gestion De Trainers ===
1. Crear Trainers
2. Editar Trainers
3. Listar Trainers Totales
4. Asignar disponibilidad y rutas
5. Listar Trainers activos.
0. Salir
""")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

def SubGestionRutas():
    while True:
        try:
            print("""
=== Gestion de Rutas ===
1. Crear nueva ruta de entrenamiento.
2. Listar rutas existentes.
3. Gestionar módulos dentro de ruta
4. Definir SGBD principal y alterno.
0. Salir
""")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

def SubGestionModulos():
    while True:
        try:
            print("""
=== Gestion de Modulos ===
1. Crear Modulos de la Ruta
2. Editar Modulos de la Ruta
0. Salir
""")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

def SubGestionAreasSalones():
    while True:
        try:
            print("""
=== Gestion de Areas/Salones ===
1. Ver áreas disponibles y su capacidad
2. Consultar disponibilidad de cupos por franja de 4h.
3. Crear Nueva Area/Salon
0. Salir
""")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

def SubMatriculas():
    while True:
        try:
            print("""
=== Gestion de Matriculas ===
1. Crear matrícula
2. Listar matrículas activas.
3. Cerrar matrícula
0. Salir
""")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

def SubReportes():
    while True:
        try:
            print("""
=== Gestion de Reportes ===
1. Listar campers inscritos.
2. Listar campers aprobados examen inicial.
3. Listar trainers activos.
4. Listar campers con bajo rendimiento.
5. Asociaciones camper–trainer–ruta.
6.Estadísticas de aprobados y perdidos por módulo, ruta y trainer.
7. Campers en riesgo alto.
0. Salir
""")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

#Menu Trainer
def menuTrainer():
    while True:
        try:
            util.Limpiar_consola()

            print("""
=== Menu Trainer ===
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

"""
Sub Menus del Coordinador
"""
def SubInformacionTrainer():
    while True:
        try:
            print("""
=== Mi Informacion ===
1. Ver mis datos personales.
2. Ver rutas que puedo dictar.
3. Ver disponibilidad de horario (slots asignados).
0. Salir
""")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

def SubCamperAsignadosTrainer():
    while True:
        try:
            print("""
=== Gestion Campers Asignados ===
1. Listar campers de mi grupo actual.
2. Consultar datos de un camper.
0. Salir
""")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

def SubRegistrarNotasCamper():
    while True:
        try:
            print("""
=== Gestion De Resgistro Notas ===
1. Seleccionar módulo actual.
2. Seleccionar camper.
3. Ingresar 3 notas: teoría, práctica, actividades.
4. Calcular automáticamente nota final.
5. Guardar en el historial del camper (y marcar aprobado/bajo rendimiento).
0. Salir
""")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

def SubResultadosCampers():
    while True:
        try:
            print("""
=== Gestion Resultados de mis Campers ===
1. Ver notas por módulo de mis campers.
2. Filtrar campers aprobados / con bajo rendimiento.
3. Exportar Reporte
0. Salir
""")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

#Menu Campers
def menuCamper():
    while True:
        try:
            util.Limpiar_consola()

            print("""
=== Menu Camper ===
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

"""
SubMenus Campers
"""
def SubInformacionCamper():
    while True:
        try:
            print("""
=== Gestion mi Informacion ===
1. Ver datos personales
2. Ver estado actual
3. Ver si está en “riesgo alto” o no.
0. Salir
""")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

def SubMatriculaCamper():
    while True:
        try:
            print("""
=== Gestion de Mi Matricula ===
1. Ver ruta asignada.
2. Ver trainer asignado.
3. Ver fechas de inicio y fin.
4. Ver salón y franja horaria (slot de 4h).
0. Salir
""")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break

def SubProgresoAcademicoCamper():
    while True:
        try:
            print("""
=== Gestion Mi Progreso Academico  ===
1. Ver historial de módulos cursados.
2. Mostrar notas finales de cada módulo.
3. Indicar módulos aprobados o reprobados.
4. Mostrar promedio general
0. Salir
""")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú principal.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú principal.")
            break
