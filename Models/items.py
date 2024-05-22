from typing import Optional
from pydantic import BaseModel, EmailStr

class Item(BaseModel):
    username: str
    password: str
    email: Optional[EmailStr] = None
