from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from app.schemas import safe_room


router = APIRouter(prefix="/safe-rooms", tags=["Safe Rooms"])

@router.post("/", response_model=safe_room.SafeRoomOut)
def create_safe_room(room: schemas.safe_room.SafeRoomCreate, db: Session = Depends(get_db)):
    return crud.safe_rooms.create_safe_room(db, room)

@router.get("/", response_model=list[schemas.safe_room.SafeRoomOut])
def list_safe_rooms(db: Session = Depends(get_db)):
    return crud.safe_rooms.get_all_safe_rooms(db)

@router.post("/{room_id}/assign-user/{user_id}")
def assign_user(room_id: int, user_id: int, db: Session = Depends(get_db)):
    return crud.safe_rooms.assign_user_to_safe_room(db, user_id, room_id)

@router.post("/{room_id}/remove-user/{user_id}")
def remove_user(room_id: int, user_id: int, db: Session = Depends(get_db)):
    return crud.safe_rooms.remove_user_from_safe_room(db, user_id, room_id)

@router.get("/{room_id}/users")
def get_users(room_id: int, db: Session = Depends(get_db)):
    return crud.safe_rooms.get_users_in_safe_room(db, room_id)
