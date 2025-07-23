# Domain models go here

from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True
    full_name: Optional[str] = None
