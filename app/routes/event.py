from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import events_crud
from app.database import get_db
from app.schemas import schemas
from app.utils.auth import authenticate_user
from app.utils.dependencies import admin_required  # Importar admin_required

router = APIRouter()

# Crear evento (solo para administradores)
@router.post("/", response_model=schemas.Event)
def create_event(
    event: schemas.EventCreate,
    email: str,
    password: str,
    db: Session = Depends(get_db)
):
    # Autenticar al usuario
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")

    # Crear el evento
    return events_crud.create_event(db=db, event=event)


# Obtener evento por ID
@router.get("/events/{event_id}", response_model=schemas.Event)
def read_event(event_id: int, db: Session = Depends(get_db)):
    db_event = events_crud.get_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

# Actualizar evento (solo para administradores)
@router.put("/{event_id}", response_model=schemas.Event)
def update_event(
    event_id: int,
    event: schemas.EventCreate,
    email: str,
    password: str,
    db: Session = Depends(get_db)
):
    # Autenticar al usuario
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")

    # Actualizar el evento
    updated_event = events_crud.update_event(db, event_id=event_id, event=event)
    if updated_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event


# Eliminar evento (solo para administradores)
@router.delete("/{event_id}")
def delete_event(
    event_id: int,
    email: str,
    password: str,
    db: Session = Depends(get_db)
):
    # Autenticar al usuario
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")

    # Eliminar el evento
    deleted_event = events_crud.delete_event(db, event_id=event_id)
    if deleted_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"detail": "Event deleted successfully"}

