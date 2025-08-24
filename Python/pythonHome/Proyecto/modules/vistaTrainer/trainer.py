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
        print(f"ID: {doc} | {t['Nombre']} {t['Apellido']} | Estado: {t['Estado']} | Disponibilidad: {t['Disponibilidad']}")

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
        trainer["RutasAsignadas"].append(ruta_seleccionada)
        print(f"✅ Ruta '{ruta_seleccionada}' asignada al trainer.")

    # Guardar cambios
    data["trainerCampusLands"][doc] = trainer
    corefiles.update_json(DB_CampusLands, data, ["trainerCampusLands"])
    print(f"✅ Trainer {trainer['Nombre']} actualizado correctamente.\n")

def listarTrainersActivos():
    data = corefiles.read_json(DB_CampusLands)
    trainers = data.get("trainerCampusLands", {})

    print("\n=== Trainers Activos ===")
    for doc, t in trainers.items():
        if t["Estado"].lower() == "activo":
            print(f"ID: {doc} | {t['Nombre']} {t['Apellido']} | Disponibilidad: {t['Disponibilidad']} | Rutas: {t['RutasAsignadas']}")
