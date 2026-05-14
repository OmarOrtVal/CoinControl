from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UsuarioSchema(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)
    apellido: str = Field(min_length=2, max_length=100)
    telefono: Optional[str] = Field(None, max_length=20)
    email: EmailStr
    password: str = Field(min_length=6)
