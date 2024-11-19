from sqlalchemy import Column, Integer, String, Boolean, Text, Date, DECIMAL, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)
    memberships = relationship("Membership", back_populates="user")
    created_at = Column(TIMESTAMP, default="now()")


class Model(Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    biography = Column(Text)
    portfolio_url = Column(String(255))
    booking_info = Column(Text)
    created_at = Column(TIMESTAMP, default="now()")
    events = relationship("Event", secondary="model_event", back_populates="models")


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    category = Column(String(50))
    image_url = Column(String(255))
    created_at = Column(TIMESTAMP, default="now()")


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    location = Column(String(255))
    date = Column(Date)
    description = Column(Text)
    created_at = Column(TIMESTAMP, default="now()")
    models = relationship("Model", secondary="model_event", back_populates="events")


class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    image_url = Column(String(255), nullable=False)
    price = Column(DECIMAL(10, 2))
    created_at = Column(TIMESTAMP, default="now()")


class Membership(Base):
    __tablename__ = 'memberships'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    membership_type = Column(String(50), nullable=False)
    benefits = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    created_at = Column(TIMESTAMP, default="now()")
    user = relationship("User", back_populates="memberships")


class ModelEvent(Base):
    __tablename__ = 'model_event'

    id = Column(Integer, primary_key=True, index=True)
    model_id = Column(Integer, ForeignKey('models.id'))
    event_id = Column(Integer, ForeignKey('events.id'))
    created_at = Column(TIMESTAMP, default="now()")
