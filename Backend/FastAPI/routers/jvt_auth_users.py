from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

# Algoritmo y duración del token JWT
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1  # en minutos

# Se usará como clave secreta la misma que la contraseña cifrada del usuario "Romero"
SECRET = "$2a$12$DMb6gcLkPOa45iwbnYVWN.rSIm9xBURETYhSSwjqduhGdcIoR4HEm"

# Definimos el router de autenticación
router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "No encontrado"}}
)

# Configuramos OAuth2: obtiene automáticamente el token de la cabecera Authorization
oauth2 = OAuth2PasswordBearer(tokenUrl="auth/login")

# Contexto de hash con bcrypt
crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Modelo base del usuario
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

# Modelo extendido que incluye la contraseña
class UserDB(User):
    password: str

# "Base de datos" de usuarios
users_db = {
    "Romero": {
        "username": "Romero",
        "full_name": "José Antonio",
        "email": "jarptgd@gmail.com",
        "disabled": False,
        "password": SECRET  # misma que usamos como clave secreta JWT
    },
    "Romero2": {
        "username": "Romero2",
        "full_name": "José Antonio",
        "email": "jarple90@gmail.com",
        "disabled": True,
        "password": "$2a$12$Hltb4E/MjePFUr9.mqF0heg2Ve3rfS3Ua/yY5smdmjVDWKQRpj/N64321"
    }
}

# Buscar usuario y devolver datos completos con contraseña
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

# Ruta de login: valida usuario y contraseña, y devuelve token firmado
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El usuario no existe")

    user = search_user_db(form.username)
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=400, detail="La contraseña es incorrecta")

    expiration = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)

    payload = {
        "sub": user.username,
        "exp": expiration
    }

    # Creamos el JWT usando la misma clave que el hash de contraseña
    access_token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_at": expiration.isoformat()
    }


