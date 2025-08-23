from util import login as login
from util import utilidades as util
from util import corefiles as core
from modules.vistaCamper import riesgo as riego

DB_CampusLands = 'data/CampusLands.json'
core.initialize_json(DB_CampusLands, {
    "camperCampusLands": {}
})

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
0. Salir
            ''')
            estado = int(input('Ingresa una Opcion: '))

            match estado:
                case 1:
                    estado = 'Inscrito'

                case 2:
                    estado = 'Aprobado'

                case 3:
                    estado = 'Cursando'

                case 4:
                    estado = 'Graduado'

                case 5:
                    estado = 'Expulsado'

                case 6:
                    estado = 'Retirado'

                case 0:
                    print('Regresando...')
                    break

                case _:
                    print("⚠️ Debes ingresar un número entre 1 y 6.")

            return estado


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
                    util.Limpiar_consola()
                    SubGestionCampers()

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
            opcion = int(input('Ingresa una Opcion: '))

            match opcion:
                case 1:
                    util.Limpiar_consola()
                    login.register()
                    util.Stop()
                    util.Limpiar_consola()

                case 2:
                    util.Limpiar_consola()
                    print('=== Listar Campers ===')
                    data = core.read_json(DB_CampusLands)

                    for section in ["camperCampusLands", "trainerCampusLands", "adminCampusLands"]:
                        if section in data:
                            print(f"\n--- {section} ---")
                            for user_id, info in data[section].items():
                                print(f"ID: {info['identificacion']} | Nombre: {info['Nombre']} {info['Apellido']} | Estado: {info['Estado']} | Rol: {info['rol']}")

                    input('Enter para continuar...')
                    util.Stop()
                    util.Limpiar_consola()

                case 3:
                    data = core.read_json(DB_CampusLands)

                    util.Limpiar_consola()
                    print('=== Consultar Camper Individual ===')

                    user = input('Ingresa el Documento del Camper que Quieres Consultar: ').strip()
                    encontrado = False

                    for section in ["camperCampusLands", "trainerCampusLands", "adminCampusLands"]:
                        for user_id, info in data.get(section, {}).items():
                            if info.get("identificacion") == user:
                                encontrado = True
                                print("\n=== Información del Camper ===")
                                print(f"Nombre completo: {info['Nombre']} {info['Apellido']}")
                                print(f"Documento: {info['identificacion']}")
                                print(f"Dirección: {info['Direccion']}")
                                print(f"Acudiente: {info['acudiente']}")
                                print(f"Teléfono: {info['telefono']}")
                                print(f"Rol: {info['rol']}")
                                print(f"Estado: {info['Estado']}")
                                print(f"Riesgo: {info['riesgoCamper']}")

                                print("\n--- Skill Actual ---")
                                for key, val in info["Skill"]["Skill Actual"].items():
                                    print(f"{key}: {val}")

                                print("\n--- Skills Culminadas ---")
                                for skill, notas in info["Skill"]["Skill Culminadas"].items():
                                    print(f"\n{skill}:")
                                    for key, val in notas.items():
                                        print(f"{key}: {val}")

                                print("\n--- Credenciales ---")
                                if info["Credenciales"]:
                                    for k, v in info["Credenciales"].items():
                                        print(f"{k}: {v}")

                                else:
                                    print("Sin credenciales registradas")

                                input('Enter para continuar...')
                                util.Stop()
                                util.Limpiar_consola()

                    if not encontrado:
                        print("⚠️ No se encontró un camper con ese documento.")
                        input('Enter para continuar...')
                        util.Stop()
                        util.Limpiar_consola()

                case 4:
                    util.Limpiar_consola()
                    print('=== Cambiar estado ===')

                    data = core.read_json(DB_CampusLands)

                    user = input('Ingresa el Documento del Camper que Quieres Consultar: ').strip()
                    encontrado = False

                    for section in ["camperCampusLands", "trainerCampusLands", "adminCampusLands"]:
                        for user_id, info in data.get(section, {}).items():
                            if info.get("identificacion") == user:
                                encontrado = True

                                opcion = EstadoCamper()
                                data[section][user_id]["Estado"] = opcion

                                core.update_json(DB_CampusLands, data)
                                print(f"✅ Estado del camper {info['Nombre']} actualizado a: {opcion}")

                                input('Enter para continuar...')
                                util.Stop()
                                util.Limpiar_consola()

                    if not encontrado:
                        print("⚠️ No se encontró un camper con ese documento.")
                        input('Enter para continuar...')
                        util.Stop()
                        util.Limpiar_consola()

                case 5:
                    util.Limpiar_consola()
                    print('=== Marcar/consultar riesgo ===')

                    data = core.read_json(DB_CampusLands)

                    user = input('Ingresa el Documento del Camper que Quieres Consultar: ').strip()
                    encontrado = False

                    for section in ["camperCampusLands", "trainerCampusLands", "adminCampusLands"]:
                        for user_id, info in data.get(section, {}).items():
                            if info.get("identificacion") == user:
                                encontrado = True
                                print(f"\n=== Camper encontrado: {info['Nombre']} {info['Apellido']} ===")

                                # ---- Aquí pides datos para evaluar ----
                                faltas_totales = int(input("Ingrese cantidad de inasistencias: "))
                                dias_seguidos = int(input("Ingrese cantidad de días seguidos ausente: "))
                                promedio_general = float(input("Ingrese promedio general: "))
                                skills_reprobados = int(input("Ingrese número de skills perdidos: "))
                                faltas_negativas = int(input("Ingrese número de faltas negativas (Houston): "))

                                # ---- Determinas el estado final ----
                                estado = riego.advertencias(
                                    faltas_totales,
                                    dias_seguidos,
                                    promedio_general,
                                    skills_reprobados,
                                    faltas_negativas,
                                    data, section, user_id
                                )

                                print(f"✅ Estado de riesgo actualizado: {estado}")
                                util.Stop()
                                util.Limpiar_consola()

                    if not encontrado:
                        print("⚠️ No se encontró un camper con ese documento.")
                        input('Enter para continuar...')
                        util.Stop()
                        util.Limpiar_consola()

                case 0:
                    print('Saliendo...')
                    break

                case _:
                    print('Ingresa una opcion valida entre (1 y 5)')
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
