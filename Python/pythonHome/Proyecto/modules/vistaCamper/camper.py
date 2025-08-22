from modules.util import utilidades as util
from modules.admin import admin as admin
from modules.util import corefiles as core
import modules.menu as menu

DB_CampusLands = "data/CampusLands.json"

# Inicializar estructura si no existe
core.initialize_json(DB_CampusLands, {"campers": {}})

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
    usuarios = data.get("campers", {})

    nota = util.Random()