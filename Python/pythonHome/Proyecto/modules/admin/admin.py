import modules.util.corefiles as corefiles
import modules.menu as menu
import modules.vistaCamper.riesgo as riesgo

#DataBase
DB_FileCamper = "data/camperCampusLands.json"
DB_FileTrainer = "data/trainerCampusLands.json"
DB_FileAdmin = "data/adminCampusLands.json"
DB_RutasAprendizaje = "data/rutasAprendizaje.json"

def addCamper():
    identificacion = int(input('Ingresa el Documento de Identidad del Camper: '))
    name = input('Ingresa el Nombre del Camper: ')
    apellido = input('Ingresa el Apellido del Camper: ')
    direccion = input('Ingresa la Direccion de Residencia del Camper: ')
    acudiente = input('Ingresa el Nombre de Acudiente del Camper: ')
    telefono = int(input('Ingresa el Telefono del Camper: '))
    riesgoCamper = riesgo.advertencias()

    campers = {
        identificacion: {
            "Nombre": name,
            "Apellido": apellido,
            "Direccion": direccion,
            "acudiente": acudiente,
            "telefono": telefono,
            "Estado" : "Inscrito",
            "riesgoCamper": str(riesgoCamper)
        }
    }

    corefiles.update_json(DB_FileCamper, campers, ["camperCampusLands"])
    print(f'✅ Camper {campers} creado correctamente')


def addTreiner():
    identificacion = int(input('Ingrese el Documento de identificacion del trainer: '))
    name = input('ingrese el Nombre del Trainer: ')
    apellido = input('Ingresa el Apellido del Trainer: ')
    telefono = int(input('Ingresa el Telefono del Trainer: '))
    habilidades = input('Ingresa las habilidades del trainer: ')
    stackTecnologico = input('Ingresa las Tecnologias que Trabaja: ')
    disponibilidad = int(input('Ingresa la Disponibilidad de Tiempo que Tiene el Trainer: '))
    exp = int(input('Ingresa la Experiencia del Trainer: '))

    trainer = {
        identificacion: {
            "Nombre": name,
            "Apellido": apellido,
            "Habilidades": habilidades,
            "StackTecnologico": stackTecnologico,
            "Disponibilidad": disponibilidad,
            "Experiencia": exp
        }
    }

    corefiles.update_json(DB_FileTrainer, trainer, ["trainerCampusLands.json"])
    print(f'✅ Trainer {trainer} creado correctamente')

def addAdmin():
    identificacion = int(input('Ingrese el Documento de identificacion del trainer: '))
    name = input('ingrese el Nombre del Admin: ')
    telefono = int(input('Ingresa el Telefono del Admin: '))
    apellido = input('Ingresa el Apellido del Admin: ')
    estudios = input('Ingresa el Nivel Academico: ')
    exp = int(input('Ingresa la Experiencia del Admin: '))

    admin = {
        identificacion: {
            "Nombre": name,
            "Apellido": apellido,
            "Telefono": telefono,
            "Estudios": estudios,
            "Experiencia": exp
        }
    }

    corefiles.update_json(DB_FileAdmin, admin, ["adminCampusLands"])
    print(f'✅ Admin {admin} creado correctamente')

def rutasExistentes():
    ruta = {
        "NodeJS" : {
            "Modulo 1": "Introducción a JavaScript y entorno Node.js",
            "Modulo 2": "Módulos, NPM y manejo de paquetes",
            "Modulo 3": "Express.js, APIs REST y conexión a bases de datos",
            "Modulo 4": "Proyecto",
            "Modulo 5": "Examen"
        },
        "Java" : {
            "Modulo 1": "Fundamentos de Java y POO",
            "Modulo 2": "Colecciones, Excepciones y Streams",
            "Modulo 3": "Java EE / Spring Boot y acceso a bases de datos",
            "Modulo 4": "Proyecto",
            "Modulo 5": "Examen"
        },
        "NetCore" : {
            "Modulo 1": "Fundamentos de C# y .NET Core",
            "Modulo 2": "Programación Orientada a Objetos y LINQ",
            "Modulo 3": "ASP.NET Core, APIs REST y Entity Framework",
            "Modulo 4": "Proyecto",
            "Modulo 5": "Examen"
        }
    }

def addRutasAprendizaje():
    while True:
        opcion = int('Deseas agregar una nueva ruta de aprendizaje (S/N): ').upper()
        match opcion:
            case "S":
                while True:
                    menuRuta = menu.menuRutasAprendizaje()
                    match menuRuta:
                        case 1:
                            # 1. Fundamentos de Programación
                            FundamentosProgramacion = 'Fundamentos de Programacion'
                            ruta = {
                                FundamentosProgramacion: {
                                    "Modulo 1": "Introducción a la Algoritmia",
                                    "Modulo 2": "PSeInt",
                                    "Modulo 3": "Python",
                                    "Modulo 4": "Proyecto",
                                    "Modulo 5": "Examen"
                                }
                            }

                        case 2:
                            # 2. Programación Web
                            programacionWeb = 'Programacion Web'
                            ruta = {
                                programacionWeb: {
                                    "Modulo 1": "HTML",
                                    "Modulo 2": "CSS",
                                    "Modulo 3": "Bootstrap",
                                    "Modulo 4": "Proyecto",
                                    "Modulo 5": "Examen"
                                }
                            }

                        case 3:
                            # 3. Programación Formal
                            programacionFormal = 'Programacion Formal'
                            ruta = {
                                programacionFormal: {
                                    "Modulo 1": "Java",
                                    "Modulo 2": "JavaScript",
                                    "Modulo 3": "C#",
                                    "Modulo 4": "Proyecto",
                                    "Modulo 5": "Examen"
                                }
                            }

                        case 4:
                            # 4. Bases de Datos
                            basesDatos = 'Bases de Datos'
                            ruta = {
                                basesDatos: {
                                    "Modulo 1": "MySQL (SGDB principal)",
                                    "Modulo 2": "MongoDB (alternativo NoSQL)",
                                    "Modulo 3": "PostgreSQL (alternativo SQL)",
                                    "Modulo 4": "Proyecto",
                                    "Modulo 5": "Examen"
                                }
                            }

                        case 5:
                            # 5. Backend
                            backend = 'Backend'
                            ruta = {
                                backend: {
                                    "Modulo 1": "NetCore",
                                    "Modulo 2": "Spring Boot",
                                    "Modulo 3": "NodeJS y Express",
                                    "Modulo 4": "Proyecto",
                                    "Modulo 5": "Examen"
                                }
                            }

                        case 0:
                            print('Saliendo...')
                            break

                        case _:
                            print('Ingresa una Opcion Valida')

                    corefiles.update_json(DB_RutasAprendizaje, ruta, ["rutasAprendizaje"])

            case "N":
                print('Saliendo...')
                break

            case _:
                print('Ingresa una Opcion Valida')