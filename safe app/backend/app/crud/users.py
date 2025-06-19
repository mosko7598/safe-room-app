from sqlalchemy.orm import Session
from app import models, schemas

def create_user(db: Session, user: schemas.user.UserCreate):
    db_user = models.User(name=user.name, phone=user.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_phone(db: Session, phone: str):
    return db.query(models.User).filter(models.User.phone == phone).first()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def update_user_location(db: Session, user_id: int, lat: float, lng: float):
    user = get_user(db, user_id)
    if user:
        user.current_lat = lat
        user.current_lng = lng
        db.commit()
        db.refresh(user)
    return user

def set_admin(db: Session, user_id: int, is_admin: bool):
    user = get_user(db, user_id)
    if user:
        user.is_admin = is_admin
        db.commit()
        db.refresh(user)
    return user
