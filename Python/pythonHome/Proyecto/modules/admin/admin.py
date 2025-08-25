import util.corefiles as corefiles
import modules.admin.grupos as grupos

# DataBase
DB_CampusLands = "data/CampusLands.json"
DB_RutasAprendizaje = "data/RutasAprendizaje.json"

# Estructura inicial
corefiles.initialize_json(DB_RutasAprendizaje, {"rutasAprendizaje": {}})

def addCamper():
    identificacion = input('Ingresa el Documento de Identidad del Camper: ').strip()
    rol = 'Camper'
    name = input('Ingresa el Nombre del Camper: ')
    apellido = input('Ingresa el Apellido del Camper: ')
    direccion = input('Ingresa la Direccion de Residencia del Camper: ')
    acudiente = input('Ingresa el Nombre de Acudiente del Camper: ')
    telefono = int(input('Ingresa el Telefono del Camper: '))
    riesgoCamper = 'Sin Riesgo'

    campers = {
        "identificacion": identificacion,
        "Nombre": name,
        "Apellido": apellido,
        "Direccion": direccion,
        "acudiente": acudiente,
        "telefono": telefono,
        "rol": rol,
        "Estado": "Inscrito",
        "riesgoCamper": str(riesgoCamper),
        "Grupo": None,
        "Skill": {
            "Skill Actual": {
                "Prueba": 0,
                "Trabajos": 0,
                "Quizes": 0,
                "Definitiva": 0
            },
            "Skill Culminadas": {
                "Nombre Skill Culminado": {
                    "Prueba": 0,
                    "Trabajos": 0,
                    "Quizes": 0,
                    "Definitiva": 0
                }
            }
        },
        "Credenciales": {}
    }

    corefiles.update_json(DB_CampusLands, {identificacion: campers}, ["camperCampusLands"])

    # 🔥 Asignar grupo y ruta automáticamente
    grupos.agregarCamperAGrupo(identificacion)

    print(f'✅ Camper {name} {apellido} creado correctamente')
    return campers

def addTrainer():
    identificacion = input('Ingrese el Documento de identificación del trainer: ').strip()
    name = input('Ingrese el Nombre del Trainer: ').strip()
    apellido = input('Ingrese el Apellido del Trainer: ').strip()
    telefono = input('Ingrese el Teléfono del Trainer: ').strip()
    email = input('Ingrese el Email del Trainer: ').strip()
    direccion = input('Ingrese la Dirección del Trainer: ').strip()
    habilidades = input('Ingrese las habilidades del Trainer: ').strip()
    stackTecnologico = input('Ingrese las tecnologías que maneja: ').strip()
    disponibilidad = input('Ingrese la disponibilidad (ej: Full-time, Medio tiempo, Horas): ').strip()
    exp = input('Ingrese los años de experiencia del Trainer: ').strip()

    trainer = {
        "identificacion": identificacion,
        "Nombre": name,
        "Apellido": apellido,
        "Telefono": telefono,
        "Email": email,
        "Direccion": direccion,
        "Habilidades": habilidades,
        "StackTecnologico": stackTecnologico,
        "Disponibilidad": disponibilidad,
        "Experiencia": exp,
        "Rol": "trainer",
        "Estado": "Activo",
        "RutasAsignadas": [],
        "Credenciales": {},
        "GruposAsignados": []
    }

    # ✅ Guardar el trainer en CampusLands.json con su identificación como clave
    corefiles.update_json(DB_CampusLands, {identificacion: trainer}, ["trainerCampusLands"])

    # ✅ Intentar asignar trainer automáticamente a un grupo disponible
    grupos.asignarTrainerDisponible(identificacion)

    print(f'✅ Trainer {name} {apellido} creado correctamente.')
    input('Enter para Continuar...')
    return trainer

def addAdmin():
    identificacion = input('Ingrese el Documento de identificacion del Admin: ').strip()
    name = input('Ingrese el Nombre del Admin: ').strip()
    telefono = input('Ingresa el Telefono del Admin: ').strip()
    apellido = input('Ingresa el Apellido del Admin: ').strip()
    estudios = input('Ingresa el Nivel Academico: ').strip()
    exp = input('Ingresa la Experiencia del Admin: ').strip()

    admin = {
        identificacion: {
            "Nombre": name,
            "Apellido": apellido,
            "Telefono": telefono,
            "Estudios": estudios,
            "Experiencia": exp,
            "Estado": "Activo",
            "Rol": "Admin"
        }
    }

    corefiles.update_json(DB_CampusLands, admin, ["adminCampusLands"])
    print(f'✅ Admin {name} {apellido} creado correctamente')

    corefiles.update_json(DB_CampusLands, admin, ["adminCampusLands"])
    print(f'✅ Admin {name} {apellido} creado correctamente')

def editarAdmin():
    identificacion = input("Ingrese el Documento del Admin a editar: ").strip()
    data = corefiles.read_json(DB_CampusLands)

    if identificacion not in data.get("adminCampusLands", {}):
        print("❌ Admin no encontrado.")
        return

    campo = input("¿Qué campo quieres editar? (Nombre, Apellido, Telefono, Estudios, Experiencia, Estado): ").strip()
    nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ").strip()

    data["adminCampusLands"][identificacion][campo] = nuevo_valor
    corefiles.save_json(DB_CampusLands, data)
    print(f"✅ Admin {identificacion} actualizado correctamente.")
    input('Enter Para Continuar...')

def listarAdminsTotales():
    data = corefiles.read_json(DB_CampusLands)
    for id, info in data.get("adminCampusLands", {}).items():
        print(f"- {id}: {info['Nombre']} {info['Apellido']} ({info['Estado']})")
    input('Enter Para Continuar...')


def listarAdminsActivos():
    data = corefiles.read_json(DB_CampusLands)
    for id, info in data.get("adminCampusLands", {}).items():
        if info.get("Estado") == "Activo":
            print(f"- {id}: {info['Nombre']} {info['Apellido']}")
    input('Enter Para Continuar...')
