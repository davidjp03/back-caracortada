from sqlalchemy.orm import Session
from models import models
from schemas import schemas

def create_model(db: Session, model: schemas.ModelCreate):
    db_model = models.Model(name=model.name, biography=model.biography, portfolio_url=model.portfolio_url, booking_info=model.booking_info)
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model

def get_model(db: Session, model_id: int):
    return db.query(models.Model).filter(models.Model.id == model_id).first()

def get_models(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Model).offset(skip).limit(limit).all()

def update_model(db: Session, model_id: int, model: schemas.ModelCreate):
    db_model = db.query(models.Model).filter(models.Model.id == model_id).first()
    if db_model:
        db_model.name = model.name
        db_model.biography = model.biography
        db_model.portfolio_url = model.portfolio_url
        db_model.booking_info = model.booking_info
        db.commit()
        db.refresh(db_model)
    return db_model

def delete_model(db: Session, model_id: int):
    db_model = db.query(models.Model).filter(models.Model.id == model_id).first()
    if db_model:
        db.delete(db_model)
        db.commit()
    return db_model