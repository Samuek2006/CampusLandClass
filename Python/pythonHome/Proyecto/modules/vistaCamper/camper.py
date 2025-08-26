from util import utilidades as util
from modules.admin import admin as admin
from util import corefiles as core
from util import session as session

DB_CampusLands = "data/CampusLands.json"
DB_Grupos = "data/Grupos.json"

# Inicializar estructura si no existe
core.initialize_json(DB_CampusLands, {
    "camperCampusLands": {},
    "trainerCampusLands": {},
    "adminCampusLands": {}
})

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
    input('Enter Para Continuar...')

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

def ver_datos_personales():
    """
    Muestra los datos personales del camper logueado.
    """
    data = core.read_json(DB_CampusLands)
    user_id = session.session.get("user_id")

    if not user_id:
        print("❌ No hay sesión activa.")
        return

    camper = data["camperCampusLands"].get(user_id)
    if not camper:
        print("❌ No se encontró información del camper.")
        return

    print("=== 📌 Datos Personales ===")
    print(f"ID: {user_id}")
    print(f"Nombre: {camper.get('Nombre', 'N/A')}")
    print(f"Apellido: {camper.get('Apellido', 'N/A')}")
    print(f"Edad: {camper.get('Edad', 'N/A')}")
    print(f"Teléfono: {camper.get('telefono', 'N/A')}")
    print(f"Correo: {camper.get('Credenciales', {}).get('correo', 'N/A')}")

    input('Enter Para Continuar...')

def ver_estado_actual():
    """
    Muestra el estado actual del camper (activo, en curso, retirado, etc.)
    """
    data = core.read_json(DB_CampusLands)
    user_id = session.session.get("user_id")

    if not user_id:
        print("❌ No hay sesión activa.")
        return

    camper = data["camperCampusLands"].get(user_id)
    if not camper:
        print("❌ No se encontró información del camper.")
        return

    estado = camper.get("Estado", "No definido")
    print("=== 📌 Estado Actual ===")
    print(f"Estado: {estado}")

    input('Enter Para Continuar...')

def verificar_riesgo():
    """
    Indica si el camper está en riesgo alto según su promedio de notas.
    """
    data = core.read_json(DB_CampusLands)
    user_id = session.session.get("user_id")

    if not user_id:
        print("❌ No hay sesión activa.")
        return

    camper = data["camperCampusLands"].get(user_id)
    if not camper:
        print("❌ No se encontró información del camper.")
        return

    historial = camper.get("Historial", {})
    if not historial:
        print("⚠️ No hay notas registradas todavía.")
        return

    # Calcular promedio de todas las notas finales registradas
    notas_finales = [mod.get("NotaFinal", 0) for mod in historial.values()]
    if not notas_finales:
        print("⚠️ No hay notas finales para calcular riesgo.")
        return

    promedio = sum(notas_finales) / len(notas_finales)
    print("=== 📌 Riesgo Académico ===")
    print(f"Promedio General: {promedio:.2f}")

    if promedio < 3.0:
        print("⚠️ El camper está en RIESGO ALTO 🚨")
    else:
        print("✅ El camper está en buen rendimiento.")

    input('Enter Para Continuar...')

def ver_ruta_asignada():
    """
    Muestra la ruta asignada al camper logueado según su grupo en grupos.json.
    """
    data_campus = core.read_json(DB_CampusLands)
    data_grupos = core.read_json(DB_Grupos)
    user_id = session.session.get("user_id")

    if not user_id:
        print("❌ No hay sesión activa.")
        return

    camper = data_campus["camperCampusLands"].get(user_id, {})
    grupo_nombre = camper.get("Grupo")  # Ejemplo: "Grupo 2"

    print("=== 🎓 Ruta Asignada ===")
    if not grupo_nombre:
        print("⚠️ No tienes grupo asignado aún.")
        return

    # Buscar en grupos.json cuál grupo tiene ese nombre
    ruta_asignada = None
    for grupo_id, grupo_info in data_grupos.get("grupos", {}).items():
        if grupo_info.get("nombre") == grupo_nombre:
            ruta_asignada = grupo_info.get("ruta")
            break

    if ruta_asignada:
        print(f"📌 {grupo_nombre} → Ruta: {ruta_asignada}")
    else:
        print(f"⚠️ No se encontró la ruta para {grupo_nombre} en grupos.json.")

    input('Enter Para Continuar...')

def ver_trainer_asignado():
    """
    Muestra el trainer asignado al camper según su grupo en grupos.json.
    """
    data_campus = core.read_json(DB_CampusLands)
    data_grupos = core.read_json(DB_Grupos)
    user_id = session.session.get("user_id")

    if not user_id:
        print("❌ No hay sesión activa.")
        return

    camper = data_campus["camperCampusLands"].get(user_id, {})
    grupo_nombre = camper.get("Grupo")  # Ejemplo: "Grupo 2"

    print("=== 👨‍🏫 Trainer Asignado ===")
    if not grupo_nombre:
        print("⚠️ No tienes grupo asignado aún.")
        return

    # Buscar en grupos.json cuál grupo tiene ese nombre
    trainer_id = None
    for grupo_id, grupo_info in data_grupos.get("grupos", {}).items():
        if grupo_info.get("nombre") == grupo_nombre:
            trainer_id = grupo_info.get("trainer")
            break

    if not trainer_id:
        print(f"⚠️ El grupo {grupo_nombre} no tiene un trainer asignado.")
        return

    # Buscar al trainer en CampusLands.json
    trainer = data_campus.get("trainerCampusLands", {}).get(str(trainer_id))
    if trainer:
        nombre = f"{trainer.get('Nombre', '')} {trainer.get('Apellido', '')}".strip()
        email = trainer.get("Email", "Sin correo")
        telefono = trainer.get("Telefono", "Sin teléfono")

        print(f"📌 Grupo: {grupo_nombre}")
        print(f"👨‍🏫 Trainer: {nombre}")
        print(f"📧 Email: {email}")
        print(f"📱 Teléfono: {telefono}")
    else:
        print(f"⚠️ No se encontró la información del trainer con ID {trainer_id}.")

    input('Enter Para Continuar...')

def ver_fechas_matricula():
    """
    Muestra las fechas de inicio y fin de la matrícula.
    """
    data = core.read_json(DB_CampusLands)
    user_id = session.session.get("user_id")

    if not user_id:
        print("❌ No hay sesión activa.")
        return

    camper = data["camperCampusLands"].get(user_id, {})
    matricula = camper.get("Matricula", {})

    inicio = matricula.get("FechaInicio")
    fin = matricula.get("FechaFin")

    print("=== 📅 Fechas de Matrícula ===")
    if inicio and fin:
        print(f"📌 Inicio: {inicio}")
        print(f"📌 Fin: {fin}")
    else:
        print("⚠️ No tienes fechas asignadas aún.")

def ver_salon_horario():
    """
    Muestra el salón y franja horaria asignada (4 horas).
    """
    data = core.read_json(DB_CampusLands)
    user_id = session.session.get("user_id")

    if not user_id:
        print("❌ No hay sesión activa.")
        return

    camper = data["camperCampusLands"].get(user_id, {})
    matricula = camper.get("Matricula", {})

    salon = matricula.get("Salon")
    horario = matricula.get("Horario")

    print("=== 🏫 Salón y Horario ===")
    if salon and horario:
        print(f"📌 Salón: {salon}")
        print(f"📌 Horario: {horario}")
    else:
        print("⚠️ No tienes salón u horario asignados aún.")

def ver_historial_modulos():
    """
    Muestra el historial de módulos (skills culminadas) por el camper logueado.
    """
    data = core.read_json(DB_CampusLands)
    user_id = session.session.get("user_id")

    if not user_id:
        print("❌ No hay sesión activa.")
        return

    camper = data["camperCampusLands"].get(user_id, {})
    skill_culminadas = camper.get("Skill", {}).get("Skill Culminadas", {})

    print("=== 📚 Historial de Módulos ===")
    if skill_culminadas:
        for i, (nombre_modulo, notas) in enumerate(skill_culminadas.items(), 1):
            definitiva = notas.get("Definitiva", "N/A")
            print(f"{i}. {nombre_modulo} → Nota final: {definitiva}")
    else:
        print("⚠️ Aún no tienes módulos cursados.")

    input('Enter Para Continuar...')

def ver_notas_finales():
    """
    Muestra las notas finales de cada módulo culminado por el camper logueado.
    """
    data = core.read_json(DB_CampusLands)
    user_id = session.session.get("user_id")

    if not user_id:
        print("❌ No hay sesión activa.")
        return

    camper = data["camperCampusLands"].get(user_id, {})
    skill_culminadas = camper.get("Skill", {}).get("Skill Culminadas", {})

    print("=== 📝 Notas Finales ===")
    if skill_culminadas:
        for modulo, notas in skill_culminadas.items():
            definitiva = notas.get("Definitiva", "N/A")
            print(f"📌 {modulo}: {definitiva}")
    else:
        print("⚠️ No tienes notas registradas.")

    input('Enter Para Continuar...')

def ver_aprobados_reprobados():
    """
    Indica qué módulos están aprobados o reprobados según la nota definitiva.
    Regla: aprobado si nota >= 60.
    """
    data = core.read_json(DB_CampusLands)
    user_id = session.session.get("user_id")

    if not user_id:
        print("❌ No hay sesión activa.")
        return

    camper = data["camperCampusLands"].get(user_id, {})
    skill_culminadas = camper.get("Skill", {}).get("Skill Culminadas", {})

    print("=== ✅❌ Módulos Aprobados / Reprobados ===")
    if skill_culminadas:
        for modulo, notas in skill_culminadas.items():
            definitiva = notas.get("Definitiva", None)
            if definitiva is not None:
                estado = "✅ Aprobado" if definitiva >= 60 else "❌ Reprobado"
                print(f"{modulo}: {definitiva} → {estado}")
            else:
                print(f"{modulo}: ⚠️ Sin nota registrada")
    else:
        print("⚠️ No tienes módulos registrados.")

    input('Enter Para Continuar...')

def ver_promedio_general():
    """
    Calcula y muestra el promedio general del camper
    usando las definitivas de Skill Culminadas.
    """
    data = core.read_json(DB_CampusLands)
    user_id = session.session.get("user_id")

    if not user_id:
        print("❌ No hay sesión activa.")
        return

    camper = data["camperCampusLands"].get(user_id, {})
    skill_culminadas = camper.get("Skill", {}).get("Skill Culminadas", {})

    print("=== 📊 Promedio General ===")
    definitivas = [
        notas.get("Definitiva")
        for notas in skill_culminadas.values()
        if notas.get("Definitiva") is not None
    ]

    if definitivas:
        promedio = sum(definitivas) / len(definitivas)
        print(f"📌 Tu promedio general es: {promedio:.2f}")
    else:
        print("⚠️ No tienes notas registradas.")

    input('Enter Para Continuar...')