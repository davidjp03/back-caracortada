from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import products_crud
from app.database import get_db
from app.schemas import schemas
from app.utils.auth import authenticate_user

router = APIRouter()

@router.post("/", response_model=schemas.Product)
def create_product(
    product: schemas.ProductCreate,
    email: str,
    password: str,
    db: Session = Depends(get_db)
):
    # Autenticar usuario
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")

    # Si es admin, proceder a crear el producto
    return products_crud.create_product(db=db, product=product)

# Obtener un producto por ID
@router.get("/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = products_crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# Actualizar un producto (Solo para administradores)
@router.put("/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: int,
    product: schemas.ProductCreate,
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

    # Actualizar el producto
    updated_product = products_crud.update_product(db, product_id=product_id, product=product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

# Eliminar un producto (Solo para administradores)
@router.delete("/{product_id}")
def delete_product(
    product_id: int,
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

    # Eliminar el producto
    deleted_product = products_crud.delete_product(db, product_id=product_id)
    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted successfully"}
