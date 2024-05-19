from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .api_v1 import BackendV1

def _get_frontend_dir() -> Path:
    return Path(__file__).parent.resolve() / ".frontend"

def create_server () -> None:
    server = FastAPI()
    server.mount(
        path="/",
        app=StaticFiles(directory=_get_frontend_dir(), html=True),
        name="frontend",
    )

    server.include_router(
        router=BackendV1(),
        prefix="/api/v1",
    )
    return server