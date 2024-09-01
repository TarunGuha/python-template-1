from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html

from contextlib import asynccontextmanager

from configs.routers import app_router

app = FastAPI()


@app.get("/openapi.json", include_in_schema=False)
async def openapi():
    return get_openapi(
        title=app.title, version=app.version, routes=app.routes, tags=["A", "B"]
    )


app.include_router(app_router)
