# Instala FastAPI si no lo has hecho aún:
# pip install "fastapi[all]"

from fastapi import FastAPI  # Importamos FastAPI
from routers import products  # Importamos router de productos
from routers import users # Importamos router de usuarios
from fastapi.staticfiles import StaticFiles    # Importamos StaticFiles para imagenes y ficheros
from routers import basic_auth_users
import os
from routers import jvt_auth_users # importa el nuevo router con JWT

app = FastAPI()  # Instanciamos la aplicación

# Ruta principal que devuelve un mensaje de bienvenida
@app.get("/") 
async def root():
    return {"mensaje": "Hola FastAPI, soy José Antonio Romero Pérez"}

# Ruta con mi URL de GitHub personal
@app.get("/url")
async def url():
    return {"url": "https://github.com/Jarple90"}

# Incluimos los routers para modularizar las rutas por temática
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static",StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")),name="static")
app.include_router(basic_auth_users.router)
app.include_router(jvt_auth_users.router)  # inclúyelo en tu app principal
"""
Una vez ejecutado hay que visitar la página:
http://127.0.0.1:8000/ → devolverá el mensaje de bienvenida
http://127.0.0.1:8000/docs → documentación Swagger
http://127.0.0.1:8000/redoc → documentación alternativa con Redoc

Para arrancar el servidor:
cd R:\PROYECTOS\Backend\FastAPI
python -m uvicorn main:app --reload

Para detener el servidor: CTRL + C

Puedes usar Postman o Thunder Client para hacer pruebas directamente
"""


