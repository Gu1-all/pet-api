# Arquivo principal da aplicação
# FastAPI

from fastapi import FastAPI
from app.core.config import settings
from app.routers import health
from app.routers import me

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(health.router)
app.include_router(me.router)
