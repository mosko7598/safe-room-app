from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

def create_safe_room(db: Session, room: schemas.safe_room.SafeRoomCreate):
    db_room = models.SafeRoom(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def get_all_safe_rooms(db: Session):
    return db.query(models.SafeRoom).all()

def get_safe_room_by_id(db: Session, room_id: int):
    return db.query(models.SafeRoom).filter(models.SafeRoom.id == room_id).first()

def assign_user_to_safe_room(db: Session, user_id: int, room_id: int):
    relation = models.UserSafeRoomRelation(
        user_id=user_id,
        safe_room_id=room_id,
        entered_at=datetime.utcnow(),
        is_inside=True
    )
    db.add(relation)
    db.commit()
    db.refresh(relation)
    return relation

def get_users_in_safe_room(db: Session, room_id: int):
    return db.query(models.UserSafeRoomRelation).filter(
        models.UserSafeRoomRelation.safe_room_id == room_id,
        models.UserSafeRoomRelation.is_inside == True
    ).all()

def remove_user_from_safe_room(db: Session, user_id: int, room_id: int):
    relation = db.query(models.UserSafeRoomRelation).filter(
        models.UserSafeRoomRelation.user_id == user_id,
        models.UserSafeRoomRelation.safe_room_id == room_id,
        models.UserSafeRoomRelation.is_inside == True
    ).first()

    if relation:
        relation.is_inside = False
        db.commit()
        db.refresh(relation)
    return relation
