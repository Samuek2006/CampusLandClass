import util.corefiles as corefiles
import util.utilidades as util

DB_Horarios = 'data/horarios.json'
DB_AreasSalones = "data/AreasSalones.json"
corefiles.initialize_json(DB_AreasSalones, {"areasSalones": {}})


def verAreas():
    """📋 Ver todas las áreas y su capacidad"""
    data = corefiles.read_json(DB_AreasSalones)
    areas = data.get("areasSalones", {})

    if not areas:
        print("⚠️ No hay áreas registradas aún.")
        return

    print("\n=== Áreas/Salones Disponibles ===")
    for nombre, info in areas.items():
        print(f"\n🏫 {nombre} (Capacidad: {info['Capacidad']})")
        for franja, cupos in info["Franjas"].items():
            print(f"  ⏰ {franja}: {cupos['ocupados']} ocupados / {cupos['disponibles']} disponibles")


def consultarDisponibilidad():
    """🔎 Consultar cupos disponibles en un salón por franja"""
    data = corefiles.read_json(DB_AreasSalones)
    areas = data.get("areasSalones", {})

    if not areas:
        print("⚠️ No hay áreas registradas aún.")
        return

    print("\n=== Selecciona un área para consultar ===")
    lista = list(areas.keys())
    for i, nombre in enumerate(lista, 1):
        print(f"{i}. {nombre}")

    try:
        opcion = int(input("👉 Ingresa el número del área: "))
        nombre_area = lista[opcion - 1]
    except (ValueError, IndexError):
        print("⚠️ Selección inválida.")
        return

    print(f"\n📊 Disponibilidad en {nombre_area}:")
    for franja, cupos in areas[nombre_area]["Franjas"].items():
        print(f"  ⏰ {franja}: {cupos['disponibles']} disponibles")


def crearArea():
    """➕ Crear un nuevo área/salón con franjas horarias dinámicas"""
    data = corefiles.read_json(DB_AreasSalones)
    areas = data.get("areasSalones", {})

    nombre = input("👉 Nombre del área/salón: ").strip()
    if nombre in areas:
        print("⚠️ Ese área ya existe.")
        return

    try:
        capacidad = int(input("👉 Capacidad total: "))
    except ValueError:
        print("⚠️ Ingresa un número válido.")
        return

    franjas = {}
    while True:
        franja = input("⏰ Ingresa una franja horaria (ej: 08:00-12:00) o ENTER para finalizar: ").strip()
        if not franja:
            break
        franjas[franja] = {"ocupados": 0, "disponibles": capacidad}

    areas[nombre] = {"Capacidad": capacidad, "Franjas": franjas}
    data["areasSalones"] = areas
    corefiles.write_json(DB_AreasSalones, data)
    print(f"✅ Área/Salón '{nombre}' creada con éxito.")


def asignarHorarioGrupo():
    """📌 Asignar un grupo a un área y franja horaria"""
    data_areas = corefiles.read_json(DB_AreasSalones)
    areas = data_areas.get("areasSalones", {})

    if not areas:
        print("⚠️ No hay áreas registradas aún.")
        return

    data_horarios = corefiles.read_json(DB_Horarios)
    horarios = data_horarios.get("horarios", {})

    grupo = input("👉 Nombre del grupo: ").strip()
    ruta = input("👉 Ruta asignada al grupo: ").strip()
    util.Limpiar_consola()

    # Seleccionar área
    print("\n=== Selecciona un área ===")
    lista_areas = list(areas.keys())
    for i, nombre in enumerate(lista_areas, 1):
        print(f"{i}. {nombre} (Capacidad: {areas[nombre]['Capacidad']})")

    try:
        opcion_area = int(input("👉 Ingresa el número del área: "))
        nombre_area = lista_areas[opcion_area - 1]
    except (ValueError, IndexError):
        print("⚠️ Selección inválida.")
        return

    # Seleccionar franja
    util.Limpiar_consola()
    print(f"\n=== Franjas de {nombre_area} ===")
    lista_franjas = list(areas[nombre_area]["Franjas"].keys())
    for i, franja in enumerate(lista_franjas, 1):
        cupos = areas[nombre_area]["Franjas"][franja]
        print(f"{i}. {franja} → {cupos['disponibles']} disponibles")

    try:
        opcion_franja = int(input("👉 Ingresa el número de la franja: "))
        franja = lista_franjas[opcion_franja - 1]
    except (ValueError, IndexError):
        print("⚠️ Selección inválida.")
        return

    # Validar disponibilidad
    if areas[nombre_area]["Franjas"][franja]["disponibles"] <= 0:
        print("⚠️ No hay cupos disponibles en esa franja.")
        return

    # Guardar asignación
    horarios[grupo] = {"Ruta": ruta, "Area": nombre_area, "Franja": franja}

    # Reducir un cupo
    areas[nombre_area]["Franjas"][franja]["ocupados"] += 1
    areas[nombre_area]["Franjas"][franja]["disponibles"] -= 1

    # Guardar en JSON
    data_areas["areasSalones"] = areas
    data_horarios["horarios"] = horarios
    corefiles.write_json(DB_AreasSalones, data_areas)
    corefiles.write_json(DB_Horarios, data_horarios)

    print(f"✅ Grupo '{grupo}' asignado a {nombre_area} en franja {franja}.")
