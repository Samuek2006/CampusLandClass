from util import utilidades as util
from modules.admin import admin as admin
from util import corefiles as core
from util import session as session

DB_CampusLands = "data/CampusLands.json"

# Inicializar estructura si no existe
core.initialize_json(DB_CampusLands, {"camperCampusLands": {}})

def userRegister():
    util.Limpiar_consola()
    print('=== REGISTRARSE A CAMPUSLANDS ===')
    campers = admin.addCamper()
    print('''
=== Para Poder Ingresar a CampusLands debes presentar una Pruba Logica ===

=== Logeate nuevamente para que se te Asigne la Prueba Logica ===
''')
    util.Stop()
    util.Limpiar_consola()
    return campers

def pruebaLogica(user_id: str):
    """
    Asigna una nota de examen de ingreso a un camper y actualiza su estado en el JSON.
    """
    data = core.read_json(DB_CampusLands)

    # Buscar en camperCampusLands
    if user_id in data["camperCampusLands"]:
        cuenta = data["camperCampusLands"][user_id]

        print('Presenta Tu Prueba Logica')
        util.Limpiar_consola()
        print('Presentando Prueba Logica....')
        util.Stop()
        util.Limpiar_consola()

        # Generar nota aleatoria
        nota = util.Random()
        print(f'Tu Resultado de la prueba Logica es de: {nota}')

        # Asignar estado según nota
        estado = "Aprobado" if nota >= 60 else "Reprobado"
        cuenta["Estado"] = estado
        cuenta["Nota Examen Ingreso"] = nota

        # Guardar cambios
        core.update_json(DB_CampusLands, data)

        print(f"✅ Estado actualizado: {estado}")
        input("Presiona Enter para continuar...")
    else:
        print("⚠️ No existe un camper con ese documento registrado.")
        input("Enter para continuar...")

def buscarUsuario(documento: str):
    """Busca un usuario en cualquier sección del JSON y devuelve (section, user_id, info)."""
    data = core.read_json(DB_CampusLands)
    for section in ["camperCampusLands", "trainerCampusLands", "adminCampusLands"]:
        for user_id, info in data.get(section, {}).items():
            if info.get("identificacion") == documento:
                return section, user_id, info, data
    return None, None, None, data


def mostrarInfoCamper(info: dict):
    """Muestra toda la información de un camper de forma estructurada."""
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

def calcularPromedio():
    """
    Calcula el promedio de las notas de examen de ingreso de todos los campers
    y actualiza su estado en el JSON.
    """
    data = core.read_json(DB_CampusLands)
    campers = data.get("camperCampusLands", {})

    if not campers:
        print("⚠️ No hay campers registrados en el sistema.")
        input("Enter para continuar...")
        return

    for user_id, info in campers.items():
        if "Nota Examen Ingreso" in info:  # Solo los que ya tienen nota
            nota = info["Nota Examen Ingreso"]

            if nota >= 60:
                estado = "Aprobado"
            else:
                estado = "Reprobado"

            info["Estado"] = estado

    # Guardar cambios en el JSON
    core.update_json(DB_CampusLands, data)
    print("✅ Promedios calculados y estados actualizados.")
    input("Enter para continuar...")

def listarCampersInscritos():
    data = core.read_json(DB_CampusLands)
    campers = data.get("camperCampusLands", {})
    print("\n📋 Campers Inscritos:")
    for cid, camper in campers.items():
        if camper.get("Estado") == "Inscrito":
            print(f"- {camper['Nombre']} {camper['Apellido']} ({cid})")
    input('Enter Para Continuar..')

def listarCampersAprobados():
    """
    Lista todos los campers que aprobaron el examen de ingreso.
    """
    data = core.read_json(DB_CampusLands)
    campers = data.get("camperCampusLands", {})

    aprobados = [
        (info["identificacion"], info["Nombre"], info["Apellido"], info.get("Nota Examen Ingreso", "N/A"))
        for _, info in campers.items()
        if info.get("Estado") == "Aprobado"
    ]

    if not aprobados:
        print("⚠️ No hay campers aprobados en el examen de ingreso.")
    else:
        print("\n=== Campers Aprobados ===")
        for ident, nombre, apellido, nota in aprobados:
            print(f"- {ident} | {nombre} {apellido} | Nota: {nota}")

    input("\nEnter para continuar...")

def campersBajoRendimiento():
    data = core.read_json(DB_CampusLands)
    campers = data.get("camperCampusLands", {})
    print("\n📋 Campers con Bajo Rendimiento:")
    for cid, camper in campers.items():
        skill = camper.get("Skill", {}).get("Skill Actual", {})
        definitiva = skill.get("Definitiva", 0)
        if definitiva < 60:  # regla base
            print(f"- {camper['Nombre']} {camper['Apellido']} ({cid}) "
                    f"→ Nota: {definitiva}")

def asociacionesCamperTrainerRuta():
    data = core.read_json(DB_CampusLands)
    grupos = data.get("gruposCampusLands", {})
    trainers = data.get("trainerCampusLands", {})
    campers = data.get("camperCampusLands", {})

    print("\n📋 Asociaciones Camper – Trainer – Ruta:")
    for gid, grupo in grupos.items():
        ruta = grupo.get("Ruta")
        trainer_id = grupo.get("Trainer")
        trainer_name = trainers.get(trainer_id, {}).get("Nombre", "Sin asignar")

        for cid in grupo.get("Campers", []):
            camper_name = campers.get(cid, {}).get("Nombre", "Desconocido")
            print(f"- Camper {camper_name} ({cid}) → Trainer {trainer_name} → Ruta {ruta}")
    input('Enter Para Continuar...')

def estadisticasGeneral():
    data = core.read_json(DB_CampusLands)
    campers = data.get("camperCampusLands", {})

    aprobados = sum(1 for c in campers.values() if c.get("Estado") == "Aprobado")
    perdidos = sum(1 for c in campers.values() if c.get("Estado") == "Reprobado")
    inscritos = sum(1 for c in campers.values() if c.get("Estado") == "Inscrito")

    print("\n📊 Estadísticas Generales:")
    print(f"✅ Aprobados: {aprobados}")
    print(f"❌ Reprobados: {perdidos}")
    print(f"📌 Inscritos: {inscritos}")
    input('Enter Para Continuar...')

def campersEnRiesgoAlto():
    data = core.read_json(DB_CampusLands)
    campers = data.get("camperCampusLands", {})
    print("\n⚠️ Campers en Riesgo Alto:")
    for cid, camper in campers.items():
        if camper.get("riesgoCamper") == "Alto" or camper.get("riesgoCamper") == "Expulsado":
            print(f"- {camper['Nombre']} {camper['Apellido']} ({cid}) → Riesgo: {camper['riesgoCamper']}")
    input('Enter Para Continuar...')