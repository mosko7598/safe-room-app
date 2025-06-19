from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    phone: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    is_admin: bool
    current_lat: Optional[float] = None
    current_lng: Optional[float] = None

    class Config:
        orm_mode = True
