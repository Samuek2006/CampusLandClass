import util.corefiles as corefiles
import modules.menus as menus

DB_RutasAprendizaje = "data/RutasAprendizaje.json"
DB_CampusLands = "data/CampusLands.json"

# Estructura inicial
corefiles.initialize_json(DB_RutasAprendizaje, {"rutasAprendizaje": {}})

def rutasExistentes():
    data = corefiles.read_json(DB_RutasAprendizaje)
    rutas = data.get("rutasAprendizaje", {})

    if not rutas:
        print("⚠️ No hay rutas registradas aún.")
        return {}

    print("\n=== Rutas de Aprendizaje ===")
    for nombre, modulos in rutas.items():
        print(f"\n📚 {nombre}")
        for modulo, contenido in modulos.items():
            print(f"   {modulo}: {contenido}")
    return rutas

def addRutasAprendizaje():
    while True:
        opcion = input("¿Deseas agregar una nueva ruta de aprendizaje? (S/N): ").upper()
        if opcion == "N":
            print("Saliendo del registro de rutas...")
            break
        elif opcion == "S":
            tipo = input("¿Quieres agregar una ruta predefinida (P) o crear una nueva (N)? ").upper()

            # ----------------------------
            # OPCIÓN 1: Rutas Predefinidas
            # ----------------------------
            if tipo == "P":
                menuRuta = menus.menuRutasAprendizaje()
                match menuRuta:
                    case "Fundamentos de Programacion":
                        ruta = { ... }
                    case "Programacion Web":
                        ruta = { ... }
                    case "Programacion Formal":
                        ruta = { ... }
                    case "Bases de Datos":
                        ruta = { ... }
                    case "Backend":
                        ruta = { ... }
                    case None:
                        print("Saliendo del menú de rutas predefinidas...")
                        continue

                    case _:
                        print("⚠️ Opción inválida.")
                        continue

                corefiles.update_json(DB_RutasAprendizaje, ruta, ["rutasAprendizaje"])
                print(f"✅ Ruta predefinida agregada correctamente.\n")

            # ----------------------------
            # OPCIÓN 2: Rutas Nuevas Dinámicas
            # ----------------------------
            elif tipo == "N":
                nombre_ruta = input("Ingrese el nombre de la nueva ruta: ").strip()

                try:
                    num_modulos = int(input("¿Cuántos módulos tendrá esta ruta?: "))
                except ValueError:
                    print("⚠️ Ingresa un número válido.")
                    continue

                modulos = {}
                print("\n=== Ingrese los módulos de la ruta ===")
                for i in range(1, num_modulos + 1):
                    contenido = input(f"Modulo {i}: ").strip()
                    modulos[f"Modulo {i}"] = contenido if contenido else f"Modulo {i} vacío"

                ruta = {nombre_ruta: modulos}
                corefiles.update_json(DB_RutasAprendizaje, ruta, ["rutasAprendizaje"])
                print(f"✅ Ruta '{nombre_ruta}' con {num_modulos} módulos creada correctamente.\n")

            else:
                print("⚠️ Opción inválida. Usa P para predefinida o N para nueva.")

        else:
            print("⚠️ Ingresa S o N.")

def gestionarModulosRuta():
    rutas = rutasExistentes()
    if not rutas:
        return

    nombre_ruta = input("\n👉 Ingresa el nombre exacto de la ruta a gestionar: ").strip()
    if nombre_ruta not in rutas:
        print("⚠️ Ruta no encontrada.")
        return

    modulos = rutas[nombre_ruta]

    while True:
        print(f"\n=== Gestión de módulos para la ruta '{nombre_ruta}' ===")
        for modulo, contenido in modulos.items():
            print(f"{modulo}: {contenido}")

        print("\n1. Agregar módulo")
        print("2. Eliminar módulo")
        print("0. Volver")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("⚠️ Ingresa un número válido.")
            continue

        if opcion == 1:
            nuevo_modulo = input("Nombre del nuevo módulo: ").strip()
            if nuevo_modulo:
                index = len(modulos) + 1
                modulos[f"Modulo {index}"] = nuevo_modulo
                print(f"✅ Módulo '{nuevo_modulo}' agregado.")
        elif opcion == 2:
            borrar = input("Escribe el nombre del módulo a eliminar: ").strip()
            encontrado = None
            for k, v in modulos.items():
                if v.lower() == borrar.lower():
                    encontrado = k
                    break
            if encontrado:
                del modulos[encontrado]
                print(f"✅ Módulo '{borrar}' eliminado.")
            else:
                print("⚠️ Módulo no encontrado.")
        elif opcion == 0:
            break
        else:
            print("⚠️ Opción inválida.")
            continue

        # Guardar cambios en JSON
        data = corefiles.read_json(DB_RutasAprendizaje)
        data["rutasAprendizaje"][nombre_ruta] = modulos
        corefiles.write_json(DB_RutasAprendizaje, data)

def definirSGBD():
    rutas = rutasExistentes()
    if not rutas:
        return

    nombre_ruta = menus.menuRutasAprendizaje()
    if not nombre_ruta:
        print("🚪 Cancelando asignación de SGDB...")
        return

    modulos = rutas[nombre_ruta]

    sgdb_principal = input("Ingrese SGDB principal: ").strip()
    sgdb_alterno = input("Ingrese SGDB alterno: ").strip()

    # Si la ruta ya tiene módulos, agregamos al final
    index_principal = len(modulos) + 1
    index_alterno = index_principal + 1

    modulos[f"Modulo {index_principal}"] = f"{sgdb_principal} (SGDB principal)"
    modulos[f"Modulo {index_alterno}"] = f"{sgdb_alterno} (alternativo)"

    # Guardar cambios
    data = corefiles.read_json(DB_RutasAprendizaje)
    data["rutasAprendizaje"][nombre_ruta] = modulos
    corefiles.write_json(DB_RutasAprendizaje, data)

    print(f"✅ SGDB definidos en la ruta '{nombre_ruta}' -> Principal: {sgdb_principal}, Alterno: {sgdb_alterno}")


def asignarDisponibilidadRutas():
    data = corefiles.read_json(DB_CampusLands)
    trainers = data.get("trainerCampusLands", {})

    doc = input("Ingrese el documento del Trainer: ").strip()
    if doc not in trainers:
        print("⚠️ Trainer no encontrado.")
        return

    trainer = trainers[doc]

    nueva_disponibilidad = input(f"Disponibilidad actual: {trainer['Disponibilidad']}. Nueva disponibilidad: ").strip()
    if nueva_disponibilidad:
        trainer["Disponibilidad"] = nueva_disponibilidad

    print("\n=== Rutas disponibles ===")
    rutas = rutasExistentes()
    if not rutas:
        print("⚠️ No hay rutas disponibles. Cree una primero.")
        return

    ruta = input("Ingrese el nombre exacto de la ruta a asignar (o Enter para no agregar): ").strip()
    if ruta in rutas:
        trainer["RutasAsignadas"].append(ruta)
    elif ruta:
        print("⚠️ Esa ruta no existe.")

    data["trainerCampusLands"][doc] = trainer
    corefiles.update_json(DB_CampusLands, data, ["trainerCampusLands"])
    print(f"✅ Trainer {trainer['Nombre']} actualizado con nuevas asignaciones.")
