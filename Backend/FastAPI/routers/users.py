from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter() #app = FastAPI()

# cd R:\PROYECTOS\Backend\FastAPI
# Inicia el server:
#   Opción 1: uvicorn users:app --reload
#   Opción 2: python -m uvicorn users:app --reload

# Entidad User con Pydantic
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

# Lista inicial de usuarios simulando una base de datos
users_list = [
    User(id=1, name="José Antonio", surname="Romero Pérez", url="https://github.com/Jarple90", age=35),
    User(id=2, name="Snow", surname="Ice", url="https://github.com/Jarple90", age=35),
    User(id=3, name="JARPLE90", surname="Romero Pérez", url="https://www.linkedin.com/in/jarple/", age=35)
]

# Ruta principal de bienvenida + listado de usuarios
@router.get("/users", response_model=dict) #app.get
async def get_users():
    return {
        "mensaje": "Hola users! La API de José Antonio Romero Pérez os da la bienvenida",
        "usuarios": users_list
    }

# Ruta alternativa que devuelve solo la lista sin mensaje
@router.get("/usersjson") #app.get
async def get_users_json():
    return users_list

# Obtener usuario por ID usando path
@router.get("/user/{id}") #app.get 
async def get_user_by_id(id: int):
    return search_user(id)

# Obtener usuario por ID usando query param (?id=)
@router.get("/user/") #app.get
async def get_user_by_query(id: int):
    return search_user(id)

# Crear un nuevo usuario
@router.post("/user/", status_code=201) #app.post
async def create_user(user: User):
    # Verifica si el usuario ya existe por ID
    if isinstance(search_user(user.id), User):
        return {"error": "El usuario ya existe"} #raise HTTPException(status_code=404, detail = "El usuario ya existe")
    # Agrega el nuevo usuario a la lista
    users_list.append(user)
    return {"message": f"Usuario {user.name} añadido correctamente"}

# Recuerda que Control + C en la terminal detiene el servidor

@router.put("/user/") #app.put
async def update_user(user: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True  # 💡 Aquí marcamos que lo encontró

    if not found:
        return {"error": "No se ha encontrado el usuario"}
    
    return {"message": f"Usuario {user.name} actualizado correctamente"}

@router.delete("/user/{id}") # app.delete
async def delete_user(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            break  # Salimos del bucle al encontrarlo

    if found:
        return {"message": f"Usuario con ID {id} eliminado correctamente"}
    else:
        return {"error": "Usuario no encontrado"}

# Función auxiliar para buscar usuario por ID
def search_user(id: int):
    for user in users_list:
        if user.id == id:
            return user
    return {"error": "Usuario no encontrado"}