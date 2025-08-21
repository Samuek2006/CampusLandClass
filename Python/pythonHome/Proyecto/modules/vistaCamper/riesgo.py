advertencias_count = 0   # Contador global de advertencias

def inasistencias():
    # Por faltar 21 inasistencias o 7 días seguidos se clasifica como riesgo y se da una advertencia
    pass

def skillPerdidos():
    # Por tener un promedio general de 65 se da una advertencia,
    # o por tener 4 o 5 skills perdidos (debajo de 70 puntos)
    pass

def faltas():
    # Por tener 40 faltas negativas puestas por Houston se da una advertencia
    pass

def advertencias():
    global advertencias_count  # Usamos la variable global

    if advertencias_count > 3:
        print('El camper queda expulsado de CampusLands por no cumplir')
        estado = 'Expulsado'
    elif advertencias_count > 0:
        print('El estudiante tiene riesgo de expulsión si no cumple')
        estado = 'Riesgo'
    else:
        print('El estudiante no tiene advertencias')
        estado = 'Sin Riesgo'
    return estado
