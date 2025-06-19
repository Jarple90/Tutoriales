from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# Definimos el router (puedes cambiar a app = FastAPI() si este es el archivo principal)
router = APIRouter(prefix="/auth",
    tags=["auth"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "No encontrado"}}
)

# Configuramos OAuth2 con tokenUrl apuntando a la ruta de login
oauth2 = OAuth2PasswordBearer(tokenUrl="auth/login")

# Modelo base de usuario
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

# Modelo extendido con contraseña
class UserDB(User):
    password: str

# Simulación de base de datos de usuarios
users_db = {
    "Romero": {
        "username": "Romero",
        "full_name": "José Antonio",
        "email": "jarptgd@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    "Romero2": {
        "username": "Romero2",
        "full_name": "José Antonio",
        "email": "jarple90@gmail.com",
        "disabled": True,
        "password": "654321"
    }
}

# Función auxiliar para buscar usuario
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    user = users_db.get(username)
    if user:
        return User(**users_db[username])

# Dependencia para obtener el usuario actual autenticado
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"}
        )
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario está inactivo"
        )
    return user

# Ruta para hacer login (token)
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El usuario no existe")

    user = search_user_db(form.username)
    if form.password != user.password:
        raise HTTPException(status_code=400, detail="La contraseña es incorrecta")

    return {"access_token": user.username, "token_type": "bearer"}

# Ruta protegida: requiere token válido
@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
