from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import photos_crud
import database
from schemas import schemas


router = APIRouter()

@router.post("/photos/", response_model=schemas.Photo)
def create_photo(photo: schemas.PhotoCreate, db: Session = Depends(database.SessionLocal)):
    return photos_crud.create_photo(db=db, photo=photo)

@router.get("/photos/{photo_id}", response_model=schemas.Photo)
def read_photo(photo_id: int, db: Session = Depends(database.SessionLocal)):
    db_photo = photos_crud.get_photo(db, photo_id=photo_id)
    if db_photo is None:
        raise HTTPException(status_code=404, detail="Photo not found")
    return db_photo
