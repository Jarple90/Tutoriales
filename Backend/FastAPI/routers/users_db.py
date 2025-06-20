from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId
from typing import Optional, Union

# Configuración del router de usuarios con prefijo '/userdb'
router = APIRouter(
    prefix="/userdb",
    tags=["userdb"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}}
)

# GET /userdb → devuelve todos los usuarios o uno por id con query ?id=...
@router.get("/", response_model=Union[list[User], User])
async def get_users(id: Optional[str] = None):
    if id:
        user = search_user("_id", ObjectId(id))
        if user:
            return user
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return users_schema(db_client.users.find())

# GET /userdb/{id} → devuelve usuario por parámetro en la ruta (path)
@router.get("/{id}", response_model=User)
async def get_user_by_id(id: str):
    user = search_user("_id", ObjectId(id))
    if user:
        return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# POST /userdb → crea un nuevo usuario
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    try:
        if search_user("email", user.email):
            raise HTTPException(status_code=409, detail="El usuario ya existe")

        user_dict = dict(user)
        user_dict.pop("id", None)

        inserted_id = db_client.users.insert_one(user_dict).inserted_id
        new_user = db_client.users.find_one({"_id": inserted_id})

        return User(**user_schema(new_user))

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")


# PUT /userdb → actualiza un usuario existente
@router.put("/", response_model=User)
async def update_user(user: User):
    user_dict = dict(user)
    user_dict.pop("id", None)

    result = db_client.users.find_one_and_replace(
        {"_id": ObjectId(user.id)}, user_dict
    )

    if not result:
        raise HTTPException(status_code=404, detail="No se ha actualizado el usuario")

    return search_user("_id", ObjectId(user.id))

# DELETE /userdb/{id} → elimina un usuario por ID
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):
    result = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    if not result:
        raise HTTPException(status_code=404, detail="No se ha eliminado el usuario")

# Función auxiliar para buscar usuario por campo
def search_user(field: str, key) -> Optional[User]:
    try:
        user = db_client.users.find_one({field: key})
        if user:
            return User(**user_schema(user))
    except:
        pass
    return None
