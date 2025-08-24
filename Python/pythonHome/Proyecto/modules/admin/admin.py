import util.corefiles as corefiles
import modules.vistaCamper.riesgo as riesgo
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
    riesgoCamper = riesgo.advertencias()

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
        identificacion: {
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
    }

    corefiles.update_json(DB_CampusLands, trainer, ["trainerCampusLands"])

    # 🔥 Intentar asignar trainer automáticamente a un grupo disponible
    grupos.asignarTrainerAGrupoAuto(identificacion)

    print(f'✅ Trainer {name} {apellido} creado correctamente.')

def addAdmin():
    identificacion = input('Ingrese el Documento de identificacion del Admin: ').strip()
    name = input('ingrese el Nombre del Admin: ')
    telefono = input('Ingresa el Telefono del Admin: ')
    apellido = input('Ingresa el Apellido del Admin: ')
    estudios = input('Ingresa el Nivel Academico: ')
    exp = input('Ingresa la Experiencia del Admin: ')

    admin = {
        identificacion: {
            "Nombre": name,
            "Apellido": apellido,
            "Telefono": telefono,
            "Estudios": estudios,
            "Experiencia": exp
        }
    }

    corefiles.update_json(DB_CampusLands, admin, ["adminCampusLands"])
    print(f'✅ Admin {name} {apellido} creado correctamente')
