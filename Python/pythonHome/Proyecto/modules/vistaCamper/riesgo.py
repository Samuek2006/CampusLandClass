import util.corefiles as core

DB_CampusLands = ('data/CampusLands.json')

advertencias_count = 0   # Contador global de advertencias

def inasistencias(faltas_totales:int, dias_seguidos:int) -> bool:
    return faltas_totales >= 21 or dias_seguidos >= 7

def skillPerdidos(promedio_general:float, skills_reprobados:int) -> bool:
    return promedio_general <= 65 or skills_reprobados >= 4

def faltas(faltas_negativas:int) -> bool:
    return faltas_negativas >= 40


def advertencias(faltas_totales:int, dias_seguidos:int, promedio_general:float, skills_reprobados:int, faltas_negativas:int, data:dict, section:str, user_id:str) -> str:
    """
    Calcula el estado de riesgo del camper y lo guarda en el JSON.
    """
    global advertencias_count
    advertencias_count = 0   # reset para cada cálculo

    # Verificaciones una por una
    if inasistencias(faltas_totales, dias_seguidos):
        advertencias_count += 1
    if skillPerdidos(promedio_general, skills_reprobados):
        advertencias_count += 1
    if faltas(faltas_negativas):
        advertencias_count += 1

    # Determinar estado
    if advertencias_count >= 3:
        estado = "Expulsado"
        print("❌ El camper queda expulsado de CampusLands por no cumplir.")
    elif advertencias_count > 0:
        estado = "Riesgo"
        print("⚠️ El estudiante tiene riesgo de expulsión si no cumple.")
    else:
        estado = "Sin Riesgo"
        print("✅ El estudiante no tiene advertencias.")

    # Actualizar en el JSON
    data[section][user_id]["riesgoCamper"] = estado
    if core and DB_CampusLands:
        core.update_json(DB_CampusLands, data)

    input("Enter para continuar...")
    return estado
