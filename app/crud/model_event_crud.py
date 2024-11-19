from sqlalchemy.orm import Session
from models import models
from schemas import schemas

def add_model_to_event(db: Session, model_event: schemas.ModelEventCreate):
    db_model_event = models.ModelEvent(model_id=model_event.model_id, event_id=model_event.event_id)
    db.add(db_model_event)
    db.commit()
    db.refresh(db_model_event)
    return db_model_event

def remove_model_from_event(db: Session, model_event_id: int):
    db_model_event = db.query(models.ModelEvent).filter(models.ModelEvent.id == model_event_id).first()
    if db_model_event:
        db.delete(db_model_event)
        db.commit()
    return db_model_event

def get_models_in_event(db: Session, event_id: int):
    return db.query(models.Model).join(models.ModelEvent).filter(models.ModelEvent.event_id == event_id).all()

def get_events_for_model(db: Session, model_id: int):
    return db.query(models.Event).join(models.ModelEvent).filter(models.ModelEvent.model_id == model_id).all()