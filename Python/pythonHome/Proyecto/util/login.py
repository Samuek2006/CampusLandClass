from util import corefiles as core
from util import utilidades as util
from util import session as session
from modules.admin import admin as admin
from modules.vistaCamper import camper as camper
import modules.menus as menus
import getpass, json

DB_CampusLands = 'data/CampusLands.json'

# Inicializar estructura base si no existe
core.initialize_json(DB_CampusLands, {
    "camperCampusLands": {},
    "trainerCampusLands": {},
    "adminCampusLands": {}
})

def register():
    data = core.read_json(DB_CampusLands)

    correo = input("Ingresa tu correo: ").strip()
    rol = "Camper"  # de momento solo campers

    # Validar que no exista ya el correo en ninguna sección
    for section in ["camperCampusLands", "trainerCampusLands", "adminCampusLands"]:
        for _, info in data.get(section, {}).items():
            if isinstance(info, dict) and info.get("Credenciales", {}).get("correo")==correo:
                print("❌ Este correo ya está registrado, intenta con otro.")
                return

    # Crear contraseña
    password = getpass.getpass("Crea una contraseña: ")
    confirm = getpass.getpass("Confirma tu contraseña: ")

    if password != confirm:
        print("❌ Las contraseñas no coinciden.")
        return

    # Pedir datos del camper desde vistaCamper
    print("\n📝 Ahora ingresa los datos personales del camper:")

    camper_data = camper.userRegister()
    identificacion = camper_data["identificacion"]

    data_campus = core.read_json(DB_CampusLands)
    data_campus["camperCampusLands"][identificacion]["Credenciales"] = {
        "correo": correo,
        "password": password
    }
    core.write_json(DB_CampusLands, data_campus)
    print(f"✅ Usuario {correo} registrado con éxito y camper creado.")

    util.Stop()
    util.Limpiar_consola()


def login():
    data = core.read_json(DB_CampusLands)

    correo = input("Ingresa tu correo: ").strip()
    password = getpass.getpass("Ingresa tu contraseña: ")

    # Buscar en campers, trainers, admins
    for section in ["camperCampusLands", "trainerCampusLands", "adminCampusLands"]:
        for user_id, info in data.get(section, {}).items():
            cred = info.get("Credenciales", {})
            if cred.get("correo") == correo:
                if cred.get("password") == password:
                    rol = info["rol"]

                    # Guardamos la sesión
                    session.session["is_logged_in"] = True
                    session.session["user_id"] = user_id
                    session.session["correo"] = correo
                    session.session["rol"] = rol

                    print(f"✅ Bienvenido {info.get('Nombre', 'Usuario')} (Rol: {rol})")

                    # Redirigir según rol
                    if rol == "Camper":
                        menus.menuCamper()

                    elif rol == "Trainer":
                        menus.menuTrainer()

                    elif rol == "Admin":
                        menus.menuCoordinador()

                    else:
                        print(f"⚠️ Rol desconocido: {rol}")

                    return True
                else:
                    print("❌ Contraseña incorrecta.")
                    return False

    print("❌ Usuario no encontrado.")
    return False
