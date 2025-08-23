from util import utilidades as util
from modules.admin import admin as admin
from util import corefiles as core
from util import session as session
import modules.menus as menus

DB_CampusLands = "data/CampusLands.json"

# Inicializar estructura si no existe
core.initialize_json(DB_CampusLands, {"camperCampusLands": {}})

def userRegister():
    print('=== REGISTRARSE A CAMPUSLANDS ===')
    campers = admin.addCamper()
    print('''
=== Para Poder Ingresar a CampusLands debes presentar una Pruba Logica ===

=== Logeate nuevamente para que se te Asigne la Prueba Logica ===
''')
    util.Stop()
    return campers

def pruebaLogica():
    data = core.read_json(DB_CampusLands)
    for section in ["camperCampusLands", "trainerCampusLands", "adminCampusLands"]:
        for user_id in data.get(section, {}).items():
            usuarios = data.get("camperCampusLands", {})
            if usuarios.get(user_id) == session.session["user_id"]:

                print('Presenta Tu Prueba Logica')
                util.Limpiar_consola()
                print('Presentando Prueba Logica....')
                util.Stop()
                util.Limpiar_consola()

                nota = util.Random()
                print(f'Tu Resultado de la prueba Logica es de: {nota}')

                if nota >= 60:
                    estado = 'Aprobado'
                else:
                    estado = 'Reprobado'

                cuenta = usuarios[user_id]
                cuenta["Estado"] = estado

