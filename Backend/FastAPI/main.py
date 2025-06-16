from fastapi import FastAPI  # Importamos FastAPI

app = FastAPI()  # Instanciamos la aplicación

@app.get("/") 
async def root():  # Definimos la función de manera async
    return {"mensaje": "Hola FastAPI, soy José Antonio Romero Pérez"}

### uvicorn main:app --reload python -m uvicorn main:app --reload

"""
Una vez ejecutado hay que mirar en la pagina http://127.0.0.1:8000/  donde:

Dara como correcto el GET con 200 OK y un error 404 Not Found

Detener el server: control + c
"""
