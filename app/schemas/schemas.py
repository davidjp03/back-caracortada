from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date

class UserBase(BaseModel):
    email: str
    is_admin: Optional[bool] = False

class UserCreate(BaseModel):
    email: str
    password: str
    is_admin: bool = False 

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ModelBase(BaseModel):
    name: str
    biography: Optional[str] = None
    portfolio_url: Optional[str] = None
    booking_info: Optional[str] = None

class ModelCreate(ModelBase):
    pass

class Model(ModelBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category: Optional[str] = None
    image_url: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class EventBase(BaseModel):
    name: str
    location: Optional[str] = None
    event_date: Optional[date] = None
    description: Optional[str] = None

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class PhotoBase(BaseModel):
    title: Optional[str] = None
    image_url: str
    price: Optional[float] = None

class PhotoCreate(PhotoBase):
    pass

class Photo(PhotoBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class MembershipBase(BaseModel):
    membership_type: str
    benefits: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None

class MembershipCreate(MembershipBase):
    user_id: int

class Membership(MembershipBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ModelEventBase(BaseModel):
    model_id: int
    event_id: int

class ModelEventCreate(ModelEventBase):
    pass

class ModelEvent(ModelEventBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
