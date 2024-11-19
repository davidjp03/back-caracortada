from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from app.crud import users_crud
from app import database
from app.schemas import schemas
from app.utils import auth


router = APIRouter()

# Endpoint de registro
@router.post("/register", response_model=schemas.User)
async def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = users_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return users_crud.create_user(db=db, user=user)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users", response_model=List[schemas.UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    users = users_crud.get_users(db, skip=skip, limit=limit)
    return users