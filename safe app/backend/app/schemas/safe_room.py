from pydantic import BaseModel
from typing import Optional

class SafeRoomBase(BaseModel):
    name: str
    location_description: Optional[str] = None
    latitude: float
    longitude: float
    max_capacity: Optional[int] = 999

class SafeRoomCreate(SafeRoomBase):
    pass

class SafeRoomOut(SafeRoomBase):
    id: int

    class Config:
        orm_mode = True
