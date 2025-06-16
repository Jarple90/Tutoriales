from fastapi import FastAPI
from pydantic  import BaseModel
app = FastAPI()

# Incia el server: uvicorn users: app --reload

@app.get("/users", response_model=dict)
async def users():
    return {"mensaje": "Hola users! La API de José Antonio Romero Pérez os da la bienvenida", "usuarios": users_list}


# Recuerda que Control + C en la terminar, se quita los datos

#@app.get("/usersjson")
#async def usersjson():
#    return [{"name":"José Antonio", "surname":"Romero Pérez","url": "https://github.com/Jarple90", "age": 35},
#            {"name":"Snow", "surname":"Ice","url": "https://github.com/Jarple90", "age": 35},
#            {"name":"JARPLE90", "surname":"Romero Pérez","url": "https://www.linkedin.com/in/jarple/", "age":35}]

# Entidad user

class User(BaseModel):
    name:str
    surname: str
    url: str
    age: int

users_list = [User(name = "José Antonio", surname = "Romero Pérez", url = "https://github.com/Jarple90", age = 35),
        User(name = "José Antonio", surname = "Romero Pérez", url = "https://github.com/Jarple90", age = 35),
        User(name = "Snow", surname = "Ice", url = "https://www.linkedin.com/in/jarple/", age = 35)]

@app.get("/usersjson")
async def usersjson():
    return [{"name":"José Antonio", "surname":"Romero Pérez","url": "https://github.com/Jarple90", "age": 35},
            {"name":"Snow", "surname":"Ice","url": "https://github.com/Jarple90", "age": 35},
            {"name":"JARPLE90", "surname":"Romero Pérez","url": "https://www.linkedin.com/in/jarple/", "age":35}]

@app.get("/users")
async def users():
    return users_list