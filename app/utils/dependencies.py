from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.users_crud import get_user_by_id
from app.database import get_db

def admin_required(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id=user_id)
    if not user or not user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized to perform this action.")
    return user
