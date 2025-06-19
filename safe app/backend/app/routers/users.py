from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserOut
from app.crud import users as crud_users

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = crud_users.get_user_by_phone(db, user.phone)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    return crud_users.create_user(db, user)

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud_users.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}/location")
def update_location(user_id: int, lat: float, lng: float, db: Session = Depends(get_db)):
    updated = crud_users.update_user_location(db, user_id, lat, lng)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "Location updated"}
