from util import login as login
from util import utilidades as util
from util import corefiles as corefiles
from modules.vistaCamper import riesgo as riego
from modules.vistaCamper import camper as camper
from modules.vistaTrainer import trainer as trainer
from modules.admin import rutas as rutas
from modules.admin import grupos as grupos
from modules.admin import areasSalones as areas
from modules.admin import admin as admin

DB_RutasAprendizaje = "data/RutasAprendizaje.json"
corefiles.initialize_json(DB_RutasAprendizaje, {"rutasAprendizaje": {}})

DB_CampusLands = 'data/CampusLands.json'
corefiles.initialize_json(DB_CampusLands, {
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
    try:
        data = corefiles.read_json(DB_RutasAprendizaje)
        rutas = data.get("rutasAprendizaje", {})

        if not rutas:
            print("⚠️ No hay rutas de aprendizaje registradas.")
            return None

        print("\n=== Rutas de Aprendizaje Disponibles ===")
        for i, ruta in enumerate(rutas.keys(), start=1):
            print(f"{i}. {ruta}")

        print("0. Cancelar")

        opcion = int(input("Ingresa una opción: "))
        if opcion == 0:
            return None
        elif 1 <= opcion <= len(rutas):
            return list(rutas.keys())[opcion - 1]  # devuelve el nombre de la ruta
        else:
            print("⚠️ Opción fuera de rango.")
            return None

    except ValueError:
        print("❌ Error: Ingresa un número válido.")
        return None
    except Exception as e:
        print(f"⚠️ Error al mostrar menú de rutas: {e}")
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
                    util.Limpiar_consola()
                    SubAdmisiones()

                case 3:
                    util.Limpiar_consola()
                    SubGestionTrainer()

                case 4:
                    util.Limpiar_consola()
                    SubGestionRutas()

                case 5:
                    util.Limpiar_consola()
                    SubGestionAreasSalones()

                case 6:
                    util.Limpiar_consola()
                    SubMatriculas()

                case 7:
                    util.Limpiar_consola()
                    SubReportes()

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
            util.Limpiar_consola()
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
                    data = corefiles.read_json(DB_CampusLands)
                    print('=== Listar Campers ===')
                    for section in ["camperCampusLands", "trainerCampusLands", "adminCampusLands"]:
                        print(f"\n--- {section} ---")
                        for _, info in data.get(section, {}).items():
                            print(f"ID: {info['identificacion']} | Nombre: {info['Nombre']} {info['Apellido']} | Estado: {info['Estado']} | Rol: {info['rol']}")
                    util.Stop()

                case 3:
                    user = input('Documento del camper: ').strip()
                    section, user_id, info, _ = camper.buscarUsuario(user)
                    if info:
                        camper.mostrarInfoCamper(info)
                    else:
                        print("⚠️ No se encontró un camper con ese documento.")
                    util.Stop()

                case 4:
                    user = input('Documento del camper: ').strip()
                    section, user_id, info, data = camper.buscarUsuario(user)
                    if info:
                        opcion = EstadoCamper()
                        data[section][user_id]["Estado"] = opcion
                        corefiles.update_json(DB_CampusLands, data)
                        print(f"✅ Estado actualizado a: {opcion}")
                    else:
                        print("⚠️ No se encontró un camper con ese documento.")
                    util.Stop()

                case 5:
                    user = input('Documento del camper: ').strip()
                    section, user_id, info, data = camper.buscarUsuario(user)
                    if info:
                        print(f"\n=== Camper encontrado: {info['Nombre']} {info['Apellido']} ===")
                        faltas_totales = int(input("Ingrese cantidad de inasistencias: "))
                        dias_seguidos = int(input("Ingrese cantidad de días seguidos ausente: "))
                        promedio_general = float(input("Ingrese promedio general: "))
                        skills_reprobados = int(input("Ingrese número de skills perdidos: "))
                        faltas_negativas = int(input("Ingrese número de faltas negativas (Houston): "))

                        estado = riego.advertencias(
                            faltas_totales, dias_seguidos,
                            promedio_general, skills_reprobados,
                            faltas_negativas, data, section, user_id
                        )
                        print(f"✅ Estado de riesgo actualizado: {estado}")
                    else:
                        print("⚠️ No se encontró un camper con ese documento.")
                    util.Stop()

                case 0:
                    print('Saliendo...')
                    break

                case _:
                    print('Ingresa una opción válida (0-5)')
                    util.Stop()

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
            util.Limpiar_consola()
            print("""
=== Admisiones ===
1. Registrar notas de examen de ingreso
2. Calcular promedio ⇒ actualizar estado
3. Listar aprobados examen.
0. Salir
""")
            opcion = int(input('Ingresa Una Opcion: '))
            match opcion:
                case 1:
                    util.Limpiar_consola()
                    print('=== Registrar notas de examen de ingreso ===')
                    user_id = input('Ingresa el documento del Camper al Cual le asignara la Nota del examen: ').strip()
                    camper.pruebaLogica(user_id)

                case 2:
                    util.Limpiar_consola()
                    print('=== Calcular promedio y actualizar estado ===')
                    camper.calcularPromedio()

                case 3:
                    util.Limpiar_consola()
                    print('=== Listado de Campers Aprobados ===')
                    camper.listarCampersAprobados()

                case 0:
                    print('Regresando ...')
                    break

                case _:
                    print('Ingresa una opcion valida entre (1 y 3)')
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
            opcion = int(input('Ingresa una Opcion: '))

            match opcion:
                case 1:
                    util.Limpiar_consola()
                    admin.addTrainer()
                    util.Stop()
                    util.Limpiar_consola()

                case 2:
                    util.Limpiar_consola()
                    trainer.editarTrainer()
                    util.Stop()
                    util.Limpiar_consola()

                case 3:
                    util.Limpiar_consola()
                    trainer.listarTrainers()
                    util.Stop()
                    util.Limpiar_consola()

                case 4:
                    util.Limpiar_consola()
                    trainer.asignarDisponibilidadRutas()
                    util.Stop()
                    util.Limpiar_consola()

                case 5:
                    util.Limpiar_consola()
                    trainer.listarTrainersActivos()
                    util.Stop()
                    util.Limpiar_consola()

                case 0:
                    print('Saliendo...')
                    break

                case _:
                    print('Ingresa una opción válida (0-5)')
                    util.Stop()

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
3. Gestionar módulos dentro de ruta.
4. Definir SGBD principal y alterno.
0. Salir
""")
            opcion = int(input("Seleccione una opción: "))

            match opcion:
                case 1:
                    util.Limpiar_consola()
                    rutas.addRutasAprendizaje()
                    util.Limpiar_consola()

                case 2:
                    util.Limpiar_consola()
                    rutas.rutasExistentes()
                    input('Enter Para Continuar...')
                    util.Limpiar_consola()

                case 3:
                    util.Limpiar_consola()
                    rutas.gestionarModulosRuta()
                    util.Limpiar_consola()

                case 4:
                    util.Limpiar_consola()
                    rutas.definirSGBD()
                    util.Limpiar_consola()

                case 0:
                    print("Saliendo de Gestión de Rutas...")
                    break
                case _:
                    print("⚠️ Opción inválida. Intenta de nuevo.")

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
=== Gestion de Módulos ===
1. Crear módulos en una ruta
2. Editar módulos de una ruta
0. Salir
""")
            opcion = int(input("👉 Selecciona una opción: "))

            match opcion:
                case 1:  # Crear módulos
                    nombre_ruta = menuRutasAprendizaje()
                    if not nombre_ruta:
                        continue

                    data = corefiles.read_json(DB_RutasAprendizaje)
                    rutas = data.get("rutasAprendizaje", {})
                    modulos = rutas.get(nombre_ruta, {})

                    try:
                        num_modulos = int(input("¿Cuántos módulos deseas agregar?: "))
                    except ValueError:
                        print("⚠️ Ingresa un número válido.")
                        continue

                    for i in range(1, num_modulos + 1):
                        contenido = input(f"👉 Nombre del módulo {len(modulos)+1}: ").strip()
                        modulos[f"Modulo {len(modulos)+1}"] = contenido if contenido else f"Modulo {len(modulos)+1} vacío"

                    data["rutasAprendizaje"][nombre_ruta] = modulos
                    corefiles.write_json(DB_RutasAprendizaje, data)
                    print(f"✅ Se agregaron {num_modulos} módulos a la ruta '{nombre_ruta}'.")

                case 2:  # Editar módulos
                    nombre_ruta = menuRutasAprendizaje()
                    if not nombre_ruta:
                        continue

                    data = corefiles.read_json(DB_RutasAprendizaje)
                    rutas = data.get("rutasAprendizaje", {})
                    modulos = rutas.get(nombre_ruta, {})

                    if not modulos:
                        print("⚠️ Esta ruta aún no tiene módulos.")
                        continue

                    print(f"\n📚 Módulos actuales en la ruta '{nombre_ruta}':")
                    for clave, contenido in modulos.items():
                        print(f"{clave}: {contenido}")

                    try:
                        num_mod = int(input("👉 Ingresa el número de módulo a editar: "))
                    except ValueError:
                        print("⚠️ Ingresa un número válido.")
                        continue

                    clave_mod = f"Modulo {num_mod}"
                    if clave_mod not in modulos:
                        print("⚠️ Ese módulo no existe.")
                        continue

                    nuevo_contenido = input(f"✏️ Nuevo contenido para {clave_mod} (antes: {modulos[clave_mod]}): ").strip()
                    if nuevo_contenido:
                        modulos[clave_mod] = nuevo_contenido
                        data["rutasAprendizaje"][nombre_ruta] = modulos
                        corefiles.write_json(DB_RutasAprendizaje, data)
                        print(f"✅ Módulo {num_mod} actualizado correctamente.")
                    else:
                        print("⚠️ No se hicieron cambios.")
                case 0:
                    print("🚪 Saliendo de Gestión de Módulos...")
                    break

                case _:
                    print("⚠️ Opción inválida. Ingresa 0, 1 o 2.")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú de módulos.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú de módulos.")
            break

def SubGestionAreasSalones():
    while True:
        try:
            print("""
=== Gestion de Areas/Salones ===
1. Ver áreas disponibles y su capacidad
2. Consultar disponibilidad de cupos por franja de 4h
3. Crear Nueva Área/Salón
4. Asignar Grupo a Área y Franja
0. Salir
""")
            opcion = int(input("👉 Ingresa una opción: "))

            match opcion:
                case 0:
                    print("🚪 Saliendo de Gestión de Áreas/Salones...")
                    break
                case 1:
                    util.Limpiar_consola()
                    areas.verAreas()
                    input('Enter Para Continuar...')
                    util.Limpiar_consola()

                case 2:
                    util.Limpiar_consola()
                    areas.consultarDisponibilidad()
                    input('Enter Para Continuar...')
                    util.Limpiar_consola()

                case 3:
                    util.Limpiar_consola()
                    areas.crearArea()
                    input('Enter Para Continuar...')
                    util.Limpiar_consola()

                case 4:
                    util.Limpiar_consola()
                    areas.asignarHorarioGrupo()
                    input('Enter Para Continuar...')
                    util.Limpiar_consola()

                case _:
                    print("⚠️ Opción inválida. Ingresa 0-4.")

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú de áreas/salones.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú de áreas/salones.")
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
            opcion = int(input("Ingresa una opción: "))

            match opcion:
                case 1:
                    doc = input("Documento del camper: ").strip()
                    grupos.agregarCamperAGrupo(doc)
                case 2:
                    grupos.listarGruposActivos()
                case 3:
                    idGrupo = input("ID del grupo a cerrar: ").strip()
                    grupos.cerrarGrupo(idGrupo)
                case 0:
                    print("👋 Saliendo del módulo de matrículas...")
                    break
                case _:
                    print("⚠️ Opción inválida.")
        except ValueError:
            print("❌ Ingresa un número válido.")
        except (KeyboardInterrupt, EOFError):
            print("\n⛔ Saliendo del módulo de matrículas...")
            break

def SubReportes():
    while True:
        try:
            print("""
=== Gestion de Reportes ===
1. Listar campers inscritos
2. Listar campers aprobados examen inicial
3. Listar trainers activos
4. Listar campers con bajo rendimiento
5. Asociaciones camper–trainer–ruta
6. Estadísticas de aprobados y perdidos por módulo, ruta y trainer
7. Campers en riesgo alto
0. Salir
""")

            opcion = input("Selecciona una opción: ").strip()

            match opcion:
                case "1":
                    util.Limpiar_consola()
                    print("📋 Reporte: Campers inscritos")
                    camper.listarCampersInscritos()
                    util.Limpiar_consola()

                case "2":
                    util.Limpiar_consola()
                    print("📋 Reporte: Campers aprobados examen inicial")
                    camper.listarCampersAprobados()
                    util.Limpiar_consola()

                case "3":
                    util.Limpiar_consola()
                    print("📋 Reporte: Trainers activos")
                    trainer.listarTrainersActivos()
                    util.Limpiar_consola()

                case "4":
                    util.Limpiar_consola()
                    print("📋 Reporte: Campers con bajo rendimiento")
                    camper.campersBajoRendimiento()
                    util.Limpiar_consola()

                case "5":
                    util.Limpiar_consola()
                    print("📋 Reporte: Asociaciones camper–trainer–ruta")
                    camper.asociacionesCamperTrainerRuta()
                    util.Limpiar_consola()

                case "6":
                    util.Limpiar_consola()
                    print("📊 Reporte: Estadísticas de aprobados y perdidos por módulo, ruta y trainer")
                    camper.estadisticasGeneral()
                    util.Limpiar_consola()

                case "7":
                    util.Limpiar_consola()
                    print("📋 Reporte: Campers en riesgo alto")
                    camper.campersEnRiesgoAlto()
                    util.Limpiar_consola()

                case "0":
                    util.Limpiar_consola()
                    print("👋 Saliendo del menú de reportes...")
                    util.Limpiar_consola()
                    break

                case _:
                    util.Limpiar_consola()
                    print("❌ Opción no válida. Intenta de nuevo.")
                    util.Limpiar_consola()

        except ValueError:
            print("❌ Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n⛔ Interrupción detectada (Ctrl+C). Cerrando menú de reportes.")
            break
        except EOFError:
            print("\n⛔ Entrada inesperada (Ctrl+D / Ctrl+Z). Cerrando menú de reportes.")
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
Sub Menus del Trainer
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
