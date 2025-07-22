from fastapi import FastAPI
from app.api.routes import user,convert

aplicacion = FastAPI(title="API de Conversión de Monedas", version="1.0.0")

aplicacion.include_router(user.router)
aplicacion.include_router(convert.router)
