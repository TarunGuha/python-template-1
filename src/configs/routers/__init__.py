from fastapi import APIRouter

from .config_router import config_router
from .websocket_router import websocket_router


app_router = APIRouter()

app_router.include_router(config_router)
# app_router.include_router(websocket_router)

__all__ = ["app_router"]
