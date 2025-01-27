from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(name=event.name, location=event.location, date=event.event_date, description=event.description)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_event(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == event_id).first()

def get_events(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Event).offset(skip).limit(limit).all()

def update_event(db: Session, event_id: int, event: schemas.EventCreate):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if db_event:
        db_event.name = event.name
        db_event.location = event.location
        db_event.date = event.event_date
        db_event.description = event.description
        db.commit()
        db.refresh(db_event)
    return db_event

def delete_event(db: Session, event_id: int):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if db_event:
        db.delete(db_event)
        db.commit()
    return db_event