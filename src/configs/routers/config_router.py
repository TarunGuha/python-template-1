from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html

from contextlib import asynccontextmanager

config_router = APIRouter()


@config_router.get(
    "/health",
    name="Check health of server",
)
def get_health_check():
    return JSONResponse(status_code=200, content={"status": "ok"})


@config_router.get("/docs", include_in_schema=False)
async def get_swagger_documentation():
    return get_swagger_ui_html(
        openapi_url=f"/openapi.json",
        title="shipment docs",
        swagger_ui_parameters={"docExpansion": None},
    )


@config_router.get("/redoc", include_in_schema=False)
async def get_redoc_documentation():
    return get_redoc_html(
        openapi_url=f"/openapi.json",
        title="shipment docs",
        with_google_fonts=True,
    )
