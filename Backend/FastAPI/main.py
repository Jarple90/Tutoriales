# Instala FastAPI si no lo has hecho aún:
# pip install "fastapi[all]"
# Si se quiere pasar de local a Cloud se puede usar CloudAtlas facil ingreso y registro "compañia", new proyect [Tres tipos de cuentas, una de ellas es gratis]
# Al crearlo podemos elegir AWS, GC y MA, además de seleccionar el páis que queremos
# Una vez ponga tu nombre y contraseña, conseguiras un link y ese lo puedes instalar en vez de la coneción local, recuerda cambiar el desplegable en client.py y en () incluir la url 

from fastapi import FastAPI  # Importamos FastAPI
from routers import products  # Importamos router de productos
from routers import users     # Importamos router de usuarios locales (simulados)
from routers import users_db  #  Importamos router que usa MongoDB
from routers import basic_auth_users  # Importamos autenticación básica
from routers import jvt_auth_users    # Importamos autenticación con JWT
from fastapi.staticfiles import StaticFiles  # Para servir archivos estáticos
import os



app = FastAPI()  # Creamos la aplicación FastAPI

# Ruta principal
@app.get("/")
async def root():
    return {"mensaje": "Hola FastAPI, soy José Antonio Romero Pérez"}

# Ruta a tu perfil de GitHub
@app.get("/url")
async def url():
    return {"url": "https://github.com/Jarple90"}

# Montamos los routers agrupados por temática
app.include_router(products.router)
app.include_router(users.router)
app.include_router(users_db.router)           # ✅ Añadimos el router que trabaja con MongoDB
app.include_router(basic_auth_users.router)
app.include_router(jvt_auth_users.router)

# Servimos archivos estáticos desde la carpeta /static
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")),
    name="static"
)

"""
Accede a tu API en el navegador:

http://127.0.0.1:8000/        → Mensaje de bienvenida
http://127.0.0.1:8000/docs    → Documentación automática Swagger
http://127.0.0.1:8000/redoc   → Documentación alternativa Redoc

Para arrancar el servidor:
cd R:\PROYECTOS\Backend\FastAPI
python -m uvicorn main:app --reload

Para detenerlo:
CTRL + C

Puedes hacer pruebas con Postman, Thunder Client o directamente desde Swagger.
"""



