def EstadoCamper():
    print('''
1. Inscrito
2. Aprobado
3. Cursando
4. Graduado
5. Expulsado
6. Retirado
            ''')
    estado = int(input('Ingresa una Opcion'))
    return estado

def menuRutasAprendizaje():
    print('''
1. Fundamentos de Programacion (Introducción a la algoritmia, PSeInt y Python)
2. Programacion Web (HTML, CSS y Bootstrap)
3. Programacion Formal (Java, JavaScript, C#)
4. Bases de datos (Mysql, MongoDb y Postgresql). Cada ruta tiene un SGDB principal y un alternativo
5. Backend (NetCore, Spring Boot, NodeJS y Express)
''')
    opcion = int(input('Ingresa una Opcion: '))
    return opcion

def menuPrincipal():
    pass
