from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, unique=True, nullable=True)
    name = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

    current_lat = Column(Float, nullable=True)
    current_lng = Column(Float, nullable=True)

    safe_room_relation = relationship("UserSafeRoomRelation", back_populates="user")

class SafeRoom(Base):
    __tablename__ = "safe_rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    location_description = Column(String, nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    max_capacity = Column(Integer, default=999)

    users_in_room = relationship("UserSafeRoomRelation", back_populates="safe_room")

class UserSafeRoomRelation(Base):
    __tablename__ = "user_safe_room_relation"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    safe_room_id = Column(Integer, ForeignKey("safe_rooms.id"))
    entered_at = Column(DateTime, default=datetime.utcnow)
    is_inside = Column(Boolean, default=True)

    user = relationship("User", back_populates="safe_room_relation")
    safe_room = relationship("SafeRoom", back_populates="users_in_room")
