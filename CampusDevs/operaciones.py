# Importamos FastAPI para crear la aplicación web
from fastapi import FastAPI, HTTPException

# Importamos BaseModel de Pydantic para definir modelos de datos
from pydantic import BaseModel

# Instanciamos la aplicación FastAPI
app = FastAPI()

# ================================
# Definición de la entidad User
# ================================
# Creamos un modelo de usuario que valida automáticamente los datos que reciba
class User(BaseModel):
    id: int
    name : str
    surname : str
    url : str
    age : int

# ================================
# Lista de usuarios simulando una "base de datos"
# ================================
userslists = [
    User(id = 1, name = "Samuel", surname = "Calderon", url = "https://samdev.com", age = 19),
    User(id = 2, name = "Felipe", surname = "Soto", url = "https://feldev.com", age = 19),
    User(id = 3, name = "Samuel", surname = "soto", url = "https://samsotdev.com", age = 19)
]

# ================================
# Rutas GET
# ================================

# Devuelve un JSON fijo (no depende de la lista de usuarios)
@app.get("/usersjson")
async def usersjson():
    return [{"name" : "Samuel", "surname" : "Calderon", "url" : "https://samdev.com", "age" : 19}]

# Devuelve la lista de usuarios (simulando la respuesta de una base de datos)
@app.get("/users")
async def users():
    return userslists

# ================================
# Ejemplo de parámetros en la URL (Path Parameters)
# ================================
# Aquí la URL incluye el id directamente: /userpath/1
@app.get("/userpath/{id}")
async def user(id: int):
    return search_user(id)

# ================================
# Ejemplo de parámetros query (Query Parameters)
# ================================
# Aquí el id se pasa como query string: /userquery/?id=1
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)

# Operaciones POST
@app.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="El usuario ya existe")
    userslists.append(user)
    return user

# Operaciones PUT
@app.put("/user/")
async def user(user: User):

    found = False
    for index, saved_user in enumerate(userslists):
        if saved_user.id == user.id:
            userslists[index] = user
            found = True

    if not found:
        return {"Error" : "No se ha podido actualizar el usuario"}
    else:
        return user

# Operaciones DELETE
@app.delete("/user/{id}")
async def user(id: int):

    found = False
    for index, saved_user in enumerate(userslists):
        if saved_user.id == id:
            del userslists[index]
            found = True

    if not found:
        return {"Error": "No se ah eliminado el usuario"}
    else:
        return {"Usuario Eliminado": id}

# ================================
# Función auxiliar para buscar un usuario por id
# ================================
def search_user(id: int):
    # Filtramos los usuarios cuyo id coincida con el solicitado
    users = filter(lambda user: user.id == id, userslists)
    try:
        # Devolvemos el primer usuario que coincida
        return list(users)[0]
    except:
        # Si no hay coincidencias devolvemos un error
        return {"Error" : "No se ha podido encontrar el usuario"}