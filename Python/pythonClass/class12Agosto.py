"""
Autor: Samuel Felipe Calderon Soto
Fecha: 12 / 08 2025
Descripcion: clase 12 agosto - Diccionarios
Tema: Diccionarios
"""
#Comentario en Linea
"""
Funciones:
    - Diccionario: Estructura de datos que almacena pares de clave-valor.

Palabras reservadas:
    - dict: Función incorporada para crear diccionarios.
    - get: Método para obtener el valor de una clave en un diccionario.
"""

agenda = {
    "nombre" : "Juan",
    "edad" : 30,
    "ciudad" : "Bogotá"
}


#Longitud
print(len(agenda))

#Conversion y creacion de diccionarios con dict()
diccionario = dict(clave1="valor1", clave2="valor2")
print(diccionario)

#update
amigo = {
    "nombre" : "Carlos"
}

llave = len(agenda) + 1

amigoDos = {
    "email" : "amigodos@example.com"
}

agenda.update(amigo)
agenda.update(amigoDos)
print(agenda)

print(agenda.get(2).get("nombre"))
claves = ["nombre", "edad", "ciudad"]
valores = ["ana", 25, "Medellín"]
diccionario = dict(zip(claves, valores))
print(diccionario)

claves = list(agenda.get(2).keys())
valores = list(agenda.get(2).values())
print(claves)
print(valores)

for item in agenda:
    print(item)

for llave,item in agenda.items():
    print(item.get('nombre'))


email = agenda.get(2).pop('email')
print(agenda)
agenda.get(2).setdefault('email', email)
print(agenda)
print(email)