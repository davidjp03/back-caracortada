from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import users_crud
import database
from schemas import schemas
from utils.dependencies import admin_required

router = APIRouter()

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.SessionLocal)):
    return users_crud.create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(database.SessionLocal)):
    db_user = users_crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/admin-only/")
def admin_action(user_id: int = Depends(admin_required)):
    return {"message": "Acción de administrador realizada con éxito."}