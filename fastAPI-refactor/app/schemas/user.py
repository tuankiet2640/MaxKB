# Pydantic schema for User
from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True
    full_name: Optional[str] = None

    class Config:
        orm_mode = True
