from sqlalchemy.orm import Session
from models import models
from schemas import schemas

def create_photo(db: Session, photo: schemas.PhotoCreate):
    db_photo = models.Photo(title=photo.title, image_url=photo.image_url, price=photo.price)
    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)
    return db_photo

def get_photos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Photo).offset(skip).limit(limit).all()

def get_photo(db: Session, photo_id: int):
    return db.query(models.Photo).filter(models.Photo.id == photo_id).first()

def delete_photo(db: Session, photo_id: int):
    db_photo = db.query(models.Photo).filter(models.Photo.id == photo_id).first()
    if db_photo:
        db.delete(db_photo)
        db.commit()
    return db_photo