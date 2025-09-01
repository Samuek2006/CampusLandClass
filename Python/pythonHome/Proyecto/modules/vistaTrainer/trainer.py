import modules.menus as menu
import util.corefiles as corefiles
import util.utilidades as util

DB_CampusLands = "data/CampusLands.json"
DB_Grupos = "data/Grupos.json"
DB_reporte_trainers_rutas = 'data/reporte_trainers_rutas.json'

def editarTrainer():
    data = corefiles.read_json(DB_CampusLands)
    trainers = data.get("trainerCampusLands", {})

    doc = input("Ingrese el documento del Trainer que desea editar: ").strip()
    if doc not in trainers:
        print("⚠️ Trainer no encontrado.")
        return

    trainer = trainers[doc]
    print(f"\n=== Editando Trainer: {trainer['Nombre']} {trainer['Apellido']} ===")

    for key in trainer.keys():
        if key in ["Rol", "RutasAsignadas", "Credenciales"]:  # no editables aquí
            continue
        nuevo_valor = input(f"{key} actual ({trainer[key]}). Nuevo valor (Enter para no cambiar): ").strip()
        if nuevo_valor:
            trainer[key] = nuevo_valor

    data["trainerCampusLands"][doc] = trainer
    corefiles.update_json(DB_CampusLands, data, ["trainerCampusLands"])
    print("✅ Trainer actualizado correctamente.")


def listarTrainers():
    data = corefiles.read_json(DB_CampusLands)
    trainers = data.get("trainerCampusLands", {})

    if not trainers:
        print("⚠️ No hay trainers registrados.")
        return

    print("\n=== Lista de Trainers ===")
    for doc, t in trainers.items():
        if isinstance(t, dict):  # ✅ Validamos que sea dict
            print(f"ID: {doc} | {t.get('Nombre', '')} {t.get('Apellido', '')} "
                  f"| Estado: {t.get('Estado', '')} | Disponibilidad: {t.get('Disponibilidad', '')}")
        else:
            print(f"⚠️ Trainer con ID {doc} tiene un formato incorrecto: {t}")
    input('Enter Para Continuar...')


def asignarDisponibilidadRutas():
    data = corefiles.read_json(DB_CampusLands)
    trainers = data.get("trainerCampusLands", {})

    doc = input("Ingrese el documento del Trainer: ").strip()
    if doc not in trainers:
        print("⚠️ Trainer no encontrado.")
        return

    trainer = trainers[doc]

    # Cambiar disponibilidad
    nueva_disponibilidad = input(f"Disponibilidad actual: {trainer['Disponibilidad']}. Nueva disponibilidad (Enter para dejar igual): ").strip()
    if nueva_disponibilidad:
        trainer["Disponibilidad"] = nueva_disponibilidad

    # Asignar ruta de aprendizaje
    print("\n--- Selección de Ruta ---")
    ruta_seleccionada = menu.menuRutasAprendizaje()
    if ruta_seleccionada:
        if "RutasAsignadas" not in trainer:
            trainer["RutasAsignadas"] = []
        if ruta_seleccionada not in trainer["RutasAsignadas"]:  # ✅ evita duplicados
            trainer["RutasAsignadas"].append(ruta_seleccionada)
            print(f"✅ Ruta '{ruta_seleccionada}' asignada al trainer.")
        else:
            print(f"⚠️ El trainer ya tiene la ruta '{ruta_seleccionada}' asignada.")

    # ✅ Guardar cambios correctamente
    corefiles.update_json(DB_CampusLands, {doc: trainer}, ["trainerCampusLands"])
    print(f"✅ Trainer {trainer['Nombre']} actualizado correctamente.\n")

#Funciones Vista Trainer
def ListarTrainesRutas():
    data = corefiles.read_json(DB_CampusLands)
    trainers = data.get("trainerCampusLands", {})

    print("\n=== Trainers Activos Y Rutas a las que esta asignado ===\n")
    for doc, t in trainers.items():
        if isinstance(t, dict):  # ✅ aseguramos que sea un diccionario
            if t.get("Estado", "").strip().lower() == "activo":
                print(f"ID: {doc} | {t.get('Nombre', '')} {t.get('Apellido', '')} | Rutas: {t.get('RutasAsignadas', [])}")

                trainerRutas = {
                    'Identificacion': doc,
                    'Nombre': t.get('Nombre', ''),
                    'Apellido': t.get('Apellido', ''),
                    'Rutas Asignadas': t.get('RutasAsignadas', [])
                }

                corefiles.update_json(DB_reporte_trainers_rutas, {doc: trainerRutas}, ['trainerRutas'])
        else:
            print(f"⚠️ Trainer con ID {doc} tiene un formato inválido: {t}")
    input('Enter Para Continuar...')

def listarTrainersActivos():
    data = corefiles.read_json(DB_CampusLands)
    trainers = data.get("trainerCampusLands", {})

    print("\n=== Trainers Activos ===")
    for doc, t in trainers.items():
        if isinstance(t, dict):  # ✅ aseguramos que sea un diccionario
            if t.get("Estado", "").strip().lower() == "activo":
                print(f"ID: {doc} | {t.get('Nombre', '')} {t.get('Apellido', '')} | "
                      f"Disponibilidad: {t.get('Disponibilidad', '')} | Rutas: {t.get('RutasAsignadas', [])}")
        else:
            print(f"⚠️ Trainer con ID {doc} tiene un formato inválido: {t}")
    input('Enter Para Continuar...')

def seleccionar_camper(grupo):
    data_grupos = corefiles.read_json(DB_Grupos)
    data_campus = corefiles.read_json(DB_CampusLands)

    campers = data_grupos["grupos"][grupo].get("campers", [])
    if not campers:
        print("❌ No hay campers en este grupo.")
        return None

    print("\n📌 Campers en el grupo:")
    for i, cid in enumerate(campers, 1):
        c = data_campus["camperCampusLands"].get(cid, {})
        print(f"{i}. {c.get('Nombre','N/A')} {c.get('Apellido','N/A')} ({cid})")

    camper_id = input("Ingrese el ID del camper a calificar: ").strip()
    if camper_id not in campers:
        print("❌ Camper no pertenece a este grupo.")
        return None

    return camper_id

def ingresar_notas():
    notas = {}
    notas["teoria"] = float(input("Nota Teoría: "))
    notas["practica"] = float(input("Nota Práctica: "))
    notas["actividades"] = float(input("Nota Actividades: "))
    return notas

def calcular_definitiva(notas):
    if None in (notas.get("teoria"), notas.get("practica"), notas.get("actividades")):
        print("⚠️ Primero ingresa todas las notas (opción 3).")
        return None
    return round(
        notas["teoria"] * 0.3 + notas["practica"] * 0.5 + notas["actividades"] * 0.2, 2
    )

def guardar_notas(camper_id, notas, data):
    data["camperCampusLands"][camper_id]["Skill"]["Skill Actual"]["Prueba"] = notas["teoria"]
    data["camperCampusLands"][camper_id]["Skill"]["Skill Actual"]["Trabajos"] = notas["practica"]
    data["camperCampusLands"][camper_id]["Skill"]["Skill Actual"]["Quizes"] = notas["actividades"]
    data["camperCampusLands"][camper_id]["Skill"]["Skill Actual"]["Definitiva"] = notas["definitiva"]

    if notas["definitiva"] < 3.0:
        data["camperCampusLands"][camper_id]["Estado"] = "Bajo Rendimiento"
    else:
        data["camperCampusLands"][camper_id]["Estado"] = "Aprobado"

    corefiles.write_json(DB_CampusLands, data)
    print(f"✅ Notas guardadas para {camper_id} - Definitiva: {notas['definitiva']}")

def seleccionar_grupo(trainer_id):
    data_grupos = corefiles.read_json(DB_Grupos)

    # Filtrar grupos del trainer
    grupos = [ (g, info) for g, info in data_grupos.get("grupos", {}).items() if info.get("trainer") == trainer_id ]

    if not grupos:
        print("❌ No tienes grupos asignados.")
        return None

    print("📌 Grupos disponibles:")
    for i, (g, info) in enumerate(grupos, 1):
        print(f"{i}. {info['nombre']} ({info['ruta']})")

    try:
        idx = int(input("Selecciona un grupo: ")) - 1
        if 0 <= idx < len(grupos):
            return grupos[idx][0]   # retorna el id del grupo
        else:
            print("⚠️ Selección inválida.")
            return None
    except ValueError:
        print("⚠️ Entrada no válida.")
        return None

def ver_notas_modulo(trainer_id):
    # Cargar los datos de los dos JSON
    data_campus = corefiles.read_json(DB_CampusLands)
    data_grupos = corefiles.read_json(DB_Grupos)

    # Buscar los grupos asignados al trainer
    grupos = [g for g, info in data_grupos.get("grupos", {}).items() if info.get("trainer") == trainer_id]
    if not grupos:
        print("❌ No tienes grupos asignados.")
        return

    # Mostrar campers y sus notas
    for grupo in grupos:
        grupo_info = data_grupos["grupos"][grupo]
        print(f"\n📌 Grupo: {grupo_info['nombre']} (ID {grupo})")

        campers = grupo_info.get("campers", [])
        if not campers:
            print("   ⚠️ No hay campers en este grupo.")
            continue

        for cid in campers:
            camper = data_campus["camperCampusLands"].get(cid)
            if not camper:
                print(f"   ❌ Camper con ID {cid} no encontrado en DB_CampusLands")
                continue

            skill = camper.get("Skill", {}).get("Skill Actual", {})
            print(f" - {camper['Nombre']} {camper['Apellido']} ({cid}) -> Definitiva: {skill.get('Definitiva', 'N/A')}")
    input('Enter Para Continuar...')

def filtrar_campers(trainer_id, estado):
    # Cargar datos de los dos JSON
    data_campus = corefiles.read_json(DB_CampusLands)
    data_grupos = corefiles.read_json(DB_Grupos)

    # Buscar los grupos asignados al trainer
    grupos = [g for g, info in data_grupos.get("grupos", {}).items() if info.get("trainer") == trainer_id]
    if not grupos:
        print("❌ No tienes grupos asignados.")
        return

    print(f"\n📊 Campers con estado: {estado}")
    for grupo in grupos:
        grupo_info = data_grupos["grupos"][grupo]
        campers = grupo_info.get("campers", [])
        if not campers:
            print(f"📌 Grupo {grupo_info['nombre']} no tiene campers.")
            continue

        for cid in campers:
            camper = data_campus["camperCampusLands"].get(cid)
            if not camper:
                print(f"❌ Camper con ID {cid} no encontrado en DB_CampusLands")
                continue

            # Normalizamos ambas comparaciones a minúsculas
            if camper.get("Estado", "").lower() == estado.lower():
                definitiva = camper.get("Skill", {}).get("Skill Actual", {}).get("Definitiva", "N/A")
                print(f" - {camper['Nombre']} {camper['Apellido']} ({cid}) -> Definitiva: {definitiva}")

    input('Enter Para Continuar...')

def exportar_reporte(trainer_id):
    print("📂 Generando reporte de campers...")

    # Cargar datos de los dos JSON
    data_campus = corefiles.read_json(DB_CampusLands)
    data_grupos = corefiles.read_json(DB_Grupos)

    # Buscar los grupos asignados al trainer
    grupos = [g for g, info in data_grupos.get("grupos", {}).items() if info.get("trainer") == trainer_id]
    if not grupos:
        print("❌ No tienes grupos asignados.")
        return

    # Recorrer grupos y campers
    for grupo in grupos:
        grupo_info = data_grupos["grupos"][grupo]
        print(f"\n📌 Grupo: {grupo_info.get('nombre', grupo)}")

        campers = grupo_info.get("campers", [])
        if not campers:
            print("   ⚠️ No hay campers en este grupo.")
            continue

        for cid in campers:
            camper = data_campus["camperCampusLands"].get(cid)
            if not camper:
                print(f"   ❌ Camper con ID {cid} no encontrado en DB_CampusLands")
                continue

            estado = camper.get("Estado", "N/A")
            definitiva = camper.get("Skill", {}).get("Skill Actual", {}).get("Definitiva", "N/A")
            print(f" - {camper['Nombre']} {camper['Apellido']} ({cid}) -> Estado: {estado}, Definitiva: {definitiva}")

    input("\nEnter para continuar...")

def SubCamperAsignadosTrainer(trainer_id):
    util.Limpiar_consola()

    # Cargar datos de los dos JSON
    data_grupos = corefiles.read_json(DB_Grupos)
    data_campus = corefiles.read_json(DB_CampusLands)

    # Buscar grupos asignados al trainer
    grupos_asignados = [
        (g, info) for g, info in data_grupos.get("grupos", {}).items()
        if info.get("trainer") == trainer_id
    ]

    if not grupos_asignados:
        print("⚠️ No tienes grupos asignados.")
    else:
        for g, grupo_info in grupos_asignados:
            print(f"\n📌 Grupo {grupo_info['nombre']} ({grupo_info['ruta']})")
            for camper_id in grupo_info.get("campers", []):
                camper = data_campus["camperCampusLands"].get(camper_id)
                if camper:
                    print(f"- {camper['Nombre']} {camper['Apellido']} ({camper_id})")

    input('Enter Para Continuar...')
    util.Stop()
    util.Limpiar_consola()