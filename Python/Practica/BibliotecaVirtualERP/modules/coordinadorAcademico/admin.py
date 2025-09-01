import util.corefiles as corefiles

DB_KnowledgeLand = 'data/KnowledgeLand.json'

corefiles.initialize_json(DB_KnowledgeLand, {
    'Estudiantes': {},
    'Bibliotecario': {},
    'CoordinadorAcademico': {}
})

def addStudent():
    identificacion = int(input('Ingresa el Documento de Identidad del Estudiante: '))
    nombre = input('Ingresa el Nombre del Estudiante: ')
    apellido = input('Ingresa el Apellido del Estudiante: ')
    carrera = input('Ingresa el Nombre de la Carrera del Estudiante: ')
    semestre = int(input('Ingresa el Semestre del Estudiante: '))
    telefono = int(input('Ingresa el Telefono del Estudiante: '))
    correo = input('Ingresa el Correo del Estudiante: ')

    Estudiantes = {
        'Identificacion': identificacion,
        'Nombre': nombre,
        'Apellido': apellido,
        'Carrera': carrera,
        'Semestre': semestre,
        'Telefono': telefono,
        'Correo': correo,
        'Estado': {
            'Libros Prestados': None,
            'Sanciones': None,
            'Reservas Pendientes': None
        }
    }

    corefiles.update_json(DB_KnowledgeLand, {identificacion: Estudiantes}, ['Estudiantes'])

    print(f'✅ Estudiante {nombre} {apellido} creado correctamente')
    return Estudiantes

def addLibrarian():
    identificacion = int(input('Ingresa el Documento de Identidad del Bibliotecario: '))
    nombre = input('Ingresa el Nombre del Bibliotecario: ')
    apellido = input('Ingresa el Apellido del Bibliotecario: ')
    telefono = int(input('Ingresa el Teléfono del Bibliotecario: '))
    correo = input('Ingresa el Correo del Bibliotecario: ')
    direccion = input('Ingresa la Dirección del Bibliotecario: ')
    fechaContratacion = input('Ingresa la Fecha de Contratación (DD/MM/AAAA): ')
    horario = input('Ingresa el Horario de Trabajo: ')
    codigoEmpleado = input('Ingresa el Código de Empleado: ')
    areaAsignada = input('Ingresa el Área Asignada en la Biblioteca: ')
    especialidad = input('Ingresa la Especialidad del Bibliotecario: ')
    estado = None

    bibliotecario = {
        'Identificacion': identificacion,
        'Nombre': nombre,
        'Apellido': apellido,
        'Telefono': telefono,
        'Correo': correo,
        'Direccion': direccion,
        'Fecha Contratacion': fechaContratacion,
        'Horario': horario,
        'Codigo Empleado': codigoEmpleado,
        'Area Asignada': areaAsignada,
        'Especialidad': especialidad,
        'Estado': estado
    }

    corefiles.update_json(DB_KnowledgeLand, {identificacion: bibliotecario}, ['Bibliotecario'])

    print(f'✅ Bibliotecario {nombre} {apellido} creado correctamente')
    return bibliotecario

def addAcademicCoordinator():
    identificacion = int(input('Ingresa el Documento de Identidad del Coordinador: '))
    nombre = input('Ingresa el Nombre del Coordinador: ')
    apellido = input('Ingresa el Apellido del Coordinador: ')
    telefono = int(input('Ingresa el Teléfono del Coordinador: '))
    correo = input('Ingresa el Correo del Coordinador: ')
    facultad = input('Ingresa la Facultad o Área Académica Asignada: ')
    oficina = input('Ingresa el Número de Oficina: ')
    extension = input('Ingresa la Extensión Telefónica Interna: ')
    horarioAtencion = input('Ingresa el Horario de Atención a Estudiantes: ')
    programas = input('Ingresa los Programas a Cargo (separados por coma): ')
    nivelAcademico = input('Ingresa el Nivel Académico Máximo (Licenciatura, Maestría, Doctorado, etc.): ')
    experiencia = input('Ingresa los Años de Experiencia en Coordinación Académica: ')
    estado = None

    coordinadorAcademico = {
        'Identificacion': identificacion,
        'Nombre': nombre,
        'Apellido': apellido,
        'Telefono': telefono,
        'Correo': correo,
        'Facultad': facultad,
        'Oficina': oficina,
        'Extencion': extension,
        'Horario Atencion': horarioAtencion,
        'Programas': programas,
        'Nivel Academico': nivelAcademico,
        'Experiencia': experiencia,
        'Estado': estado
    }

    corefiles.update_json(DB_KnowledgeLand, {identificacion: coordinadorAcademico}, ['CoordinadorAcademico'])

    print(f'✅ Coordinador Academico {nombre} {apellido} creado correctamente')
    return coordinadorAcademico