"""
Autor: Samuel Felipe Calderón Soto
Fecha: 25/07/2025
Descripcion: Este Script realiza recomendaciones de comida basadas en el clima y la hora del día.
"""

clima = input("Ingrese el clima (soleado, nublado, lluvioso): ").upper()
hora = input("Ingrese la hora del día (mañana, tarde, noche): ").upper()

match clima:
    case "SOLEADO":
        if (hora == "MAÑANA"):
            print("Recomendación: Desayuno ligero con frutas y jugo natural.")
        elif (hora == "TARDE"):
            print("Recomendación: Ensalada fresca con pollo a la parrilla.")
        elif (hora == "NOCHE"):
            print("Recomendación: Cena ligera con pescado al horno y verduras.")
        else:
            print("Hora no válida. Por favor, ingrese mañana, tarde o noche.")
    case "NUBLADO":
        if (hora == "MAÑANA"):
            print("Recomendación: Desayuno caliente con avena y frutas.")
        elif (hora == "TARDE"):
            print("Recomendación: Sopa de verduras y sándwich.")
        elif (hora == "NOCHE"):
            print("Recomendación: Cena reconfortante con pasta y salsa.")
        else:
            print("Hora no válida. Por favor, ingrese mañana, tarde o noche.")
    case "LLUVIOSO":
        if (hora == "MAÑANA"):
            print("Recomendación: Desayuno con tostadas y café.")
        elif (hora == "TARDE"):
            print("Recomendación: Té caliente y galletas.")
        elif (hora == "NOCHE"):
            print("Recomendación: Cena con estofado y pan.")
        else:
            print("Hora no válida. Por favor, ingrese mañana, tarde o noche.")