### User model ###

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None  #  opcional para permitir POST sin ID
    username: str
    full_name: str
    email: str
    disabled: bool
