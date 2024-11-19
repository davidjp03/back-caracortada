from fastapi import FastAPI
from app.routes import auth,event,product
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # La URL del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Incluir rutas de autenticación
app.include_router(auth.router, tags=["auth"])

app.include_router(event.router, tags=["events"], prefix="/events")

app.include_router(product.router, tags=["products",],prefix="/products")