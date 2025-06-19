# Archivo: routers/users.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Definimos el router
router = APIRouter()

# Modelo de usuario usando Pydantic
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

# Lista de usuarios simulando una base de datos
users_list = [
    User(id=1, name="José Antonio", surname="Romero Pérez", url="https://github.com/Jarple90", age=35),
    User(id=2, name="Snow", surname="Ice", url="https://github.com/Jarple90", age=35),
    User(id=3, name="JARPLE90", surname="Romero Pérez", url="https://www.linkedin.com/in/jarple/", age=35)
]

# GET /users → Devuelve la lista completa de usuarios
@router.get("/users")
async def get_users():
    return {
        "mensaje": "Hola users! La API de José Antonio Romero Pérez os da la bienvenida",
        "usuarios": users_list
    }

# GET /usersjson → Devuelve lista en formato JSON plano
@router.get("/usersjson")
async def get_users_json():
    return users_list

# GET /user/{id} → Obtener un usuario por ID (path)
@router.get("/user/{id}")
async def get_user_by_path(id: int):
    user = search_user(id)
    if user is None:
        return {"error": "Usuario no encontrado"}
    return user

# GET /user/?id= → Obtener un usuario por ID (query)
@router.get("/user/")
async def get_user_by_query(id: int):
    user = search_user(id)
    if user is None:
        return {"error": "Usuario no encontrado"}
    return user

# POST /user → Crear nuevo usuario
@router.post("/user/", status_code=201)
async def create_user(user: User):
    if search_user(user.id) is not None:
        raise HTTPException(status_code=409, detail="El usuario ya existe")
    users_list.append(user)
    return {"message": f"Usuario {user.name} añadido correctamente"}

# PUT /user → Actualizar usuario existente
@router.put("/user/")
async def update_user(user: User):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            return {"message": f"Usuario {user.name} actualizado correctamente"}
    return {"error": "No se ha encontrado el usuario"}

# DELETE /user/{id} → Eliminar usuario
@router.delete("/user/{id}")
async def delete_user(id: int):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            return {"message": f"Usuario con ID {id} eliminado correctamente"}
    return {"error": "Usuario no encontrado"}

# Función auxiliar para buscar usuario por ID
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except IndexError:
        return None


