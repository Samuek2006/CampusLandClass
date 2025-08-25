import util.corefiles as corefiles
import modules.admin.rutas as rutas
import modules.vistaTrainer as trainers
import modules.vistaCamper as campers

DB_Grupos = "data/Grupos.json"
DB_Rutas = "data/RutasAprendizaje.json"
DB_Trainers = "data/CampusLands.json"
DB_Campers = "data/CampusLands.json"

# Estructura inicial
corefiles.initialize_json(DB_Grupos, {"grupos": {}})

def obtenerSiguienteRuta():
    """Devuelve la siguiente ruta según cuántos grupos existen."""
    data_rutas = corefiles.read_json(DB_Rutas).get("rutasAprendizaje", {})
    data_grupos = corefiles.read_json(DB_Grupos).get("grupos", {})

    rutas_list = list(data_rutas.keys())
    if not rutas_list:
        print("⚠️ No hay rutas registradas aún.")
        return None

    indice = len(data_grupos) % len(rutas_list)
    return rutas_list[indice]


def crearGrupo():
    """Crea un nuevo grupo con la siguiente ruta disponible."""
    data = corefiles.read_json(DB_Grupos)
    grupos = data.get("grupos", {})

    idGrupo = len(grupos) + 1
    nombre = f"Grupo {idGrupo}"
    ruta_asignada = obtenerSiguienteRuta()
    if not ruta_asignada:
        return

    grupo = {
        "idGrupo": idGrupo,
        "nombre": nombre,
        "ruta": ruta_asignada,
        "trainer": None,
        "campers": [],
        "capacidadMax": 33,
        "estado": "abierto"
    }

    data["grupos"][str(idGrupo)] = grupo
    corefiles.write_json(DB_Grupos, data)
    print(f"✅ Grupo '{nombre}' creado con la ruta '{ruta_asignada}'.")
    return idGrupo


def asignarTrainerAGrupo(idGrupo, docTrainer):
    """Asigna un trainer a un grupo validando la regla de máximo 2 grupos."""
    data = corefiles.read_json(DB_Grupos)
    grupos = data.get("grupos", {})

    if str(idGrupo) not in grupos:
        print("⚠️ Grupo no encontrado.")
        return

    # Contar en cuántos grupos está el trainer
    count = sum(1 for g in grupos.values() if g["trainer"] == docTrainer)
    if count >= 2:
        print("⚠️ Ese trainer ya tiene 2 grupos asignados.")
        return

    grupos[str(idGrupo)]["trainer"] = docTrainer
    corefiles.write_json(DB_Grupos, data)
    print(f"✅ Trainer {docTrainer} asignado al grupo {idGrupo}.")


def agregarCamperAGrupo(docCamper):
    """Agrega un camper al primer grupo abierto con cupo disponible."""
    data = corefiles.read_json(DB_Grupos)
    grupos = data.get("grupos", {})

    # Buscar grupo abierto con cupo
    grupo_seleccionado = None
    for g in grupos.values():
        if g["estado"] == "abierto" and len(g["campers"]) < g["capacidadMax"]:
            grupo_seleccionado = g
            break

    # Si no existe grupo abierto → crear uno nuevo
    if not grupo_seleccionado:
        crearGrupo()
        data = corefiles.read_json(DB_Grupos)
        grupos = data.get("grupos", {})
        grupo_seleccionado = list(grupos.values())[-1]  # el último creado

    grupo_seleccionado["campers"].append(docCamper)

    # Cerrar grupo si llegó a capacidad
    if len(grupo_seleccionado["campers"]) >= grupo_seleccionado["capacidadMax"]:
        grupo_seleccionado["estado"] = "cerrado"
        print(f"🚪 Grupo {grupo_seleccionado['nombre']} cerrado (capacidad llena).")
        crearGrupo()

    data["grupos"][str(grupo_seleccionado["idGrupo"])] = grupo_seleccionado
    corefiles.write_json(DB_Grupos, data)
    print(f"✅ Camper {docCamper} agregado al grupo {grupo_seleccionado['nombre']}.")


def listarGruposActivos():
    """Muestra los grupos abiertos y su información."""
    data = corefiles.read_json(DB_Grupos)
    grupos = data.get("grupos", {})

    abiertos = [g for g in grupos.values() if g["estado"] == "abierto"]
    if not abiertos:
        print("⚠️ No hay grupos activos.")
        return

    print("\n=== Grupos Activos ===")
    for g in abiertos:
        print(f"- {g['nombre']} | Ruta: {g['ruta']} | Trainer: {g['trainer']} | Cupos: {len(g['campers'])}/{g['capacidadMax']}")


def cerrarGrupo(idGrupo):
    """Cierra un grupo manualmente."""
    data = corefiles.read_json(DB_Grupos)
    grupos = data.get("grupos", {})

    if str(idGrupo) not in grupos:
        print("⚠️ Grupo no encontrado.")
        return

    grupos[str(idGrupo)]["estado"] = "cerrado"
    corefiles.write_json(DB_Grupos, data)
    print(f"🚪 Grupo {idGrupo} cerrado manualmente.")
