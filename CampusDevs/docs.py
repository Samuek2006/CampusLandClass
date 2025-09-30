from fastapi import FastAPI

app = FastAPI()

# Url Local: http://127.0.0.1:8000/
@app.get("/")
async def root():
    return 'Hola Mundo'

# Url Local: http://127.0.0.1:8000/url
@app.get("/url")
async def url():
    return { "url": "https://kliioapp.netlify.app/"}

# Inicia un servidor Local: uvicorn main:app --reload
# Detener servidor Local: Ctrl + C

# Documentacion con Swagger: http://127.0.0.1:8000/docs
# Documentacion con Redocly: http://127.0.0.1:8000/redoc

"""
OPERACIONES BASICAS:
- POST: para crear datos.
- GET: Para leer datos.
- PUT: para actualizar datos.
- DELETE: para borrar datos.

OPERACIONES EXOTICAS:
- OPTIONS: 
- HEAD: 
- PATCH: 
- TRANCE: 
"""