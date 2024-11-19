from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import modelos_crud
import database
from schemas import schemas

router = APIRouter()

@router.post("/models/", response_model=schemas.Model)
def create_model(model: schemas.ModelCreate, db: Session = Depends(database.SessionLocal)):
    return modelos_crud.create_model(db=db, model=model)

@router.get("/models/{model_id}", response_model=schemas.Model)
def read_model(model_id: int, db: Session = Depends(database.SessionLocal)):
    db_model = modelos_crud.get_model(db, model_id=model_id)
    if db_model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return db_model
