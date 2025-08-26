import modules.menus as menu
import util.corefiles as corefiles

DB_CampusLands = "data/CampusLands.json"

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

def seleccionar_camper(grupo, data):
    campers = data["gruposCampusLands"][grupo].get("Campers", [])
    if not campers:
        print("❌ No hay campers en este grupo.")
        return None
    print("\n📌 Campers en el grupo:")
    for i, cid in enumerate(campers, 1):
        c = data["camperCampusLands"][cid]
        print(f"{i}. {c['Nombre']} {c['Apellido']} ({cid})")
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

    corefiles.save_json(DB_CampusLands, data)
    print(f"✅ Notas guardadas para {camper_id} - Definitiva: {notas['definitiva']}")

def seleccionar_grupo(trainer_id, data):
    grupos = [g for g, info in data.get("gruposCampusLands", {}).items() if info.get("Trainer") == trainer_id]
    if not grupos:
        print("❌ No tienes grupos asignados.")
        return None
    print("📌 Grupos disponibles:")
    for i, g in enumerate(grupos, 1):
        print(f"{i}. {g}")
    idx = int(input("Selecciona un grupo: ")) - 1
    return grupos[idx]

def ver_notas_modulo(trainer_id, data):
    grupos = [g for g, info in data.get("gruposCampusLands", {}).items() if info.get("Trainer") == trainer_id]
    if not grupos:
        print("❌ No tienes grupos asignados.")
        return

    for grupo in grupos:
        print(f"\n📌 Grupo: {grupo}")
        campers = data["gruposCampusLands"][grupo].get("Campers", [])
        for cid in campers:
            camper = data["camperCampusLands"][cid]
            skill = camper.get("Skill", {}).get("Skill Actual", {})
            print(f" - {camper['Nombre']} {camper['Apellido']} ({cid}) -> Definitiva: {skill.get('Definitiva', 'N/A')}")

def filtrar_campers(trainer_id, data, estado):
    grupos = [g for g, info in data.get("gruposCampusLands", {}).items() if info.get("Trainer") == trainer_id]
    if not grupos:
        print("❌ No tienes grupos asignados.")
        return

    print(f"\n📊 Campers con estado: {estado}")
    for grupo in grupos:
        campers = data["gruposCampusLands"][grupo].get("Campers", [])
        for cid in campers:
            camper = data["camperCampusLands"][cid]
            if camper.get("Estado") == estado:
                print(f" - {camper['Nombre']} {camper['Apellido']} ({cid})")


def exportar_reporte(trainer_id, data):
    # Aquí podrías armar un reporte en CSV/Excel/PDF según lo que necesites
    # Ejemplo simple en consola:
    print("📂 Generando reporte de campers...")
    grupos = [g for g, info in data.get("gruposCampusLands", {}).items() if info.get("Trainer") == trainer_id]
    for grupo in grupos:
        print(f"\nGrupo: {grupo}")
        campers = data["gruposCampusLands"][grupo].get("Campers", [])
        for cid in campers:
            camper = data["camperCampusLands"][cid]
            print(f" - {camper['Nombre']} {camper['Apellido']} ({cid}) -> Estado: {camper.get('Estado', 'N/A')}")

