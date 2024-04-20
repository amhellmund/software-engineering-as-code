from fastapi import FastAPI

from .api_v1 import BackendV1

def create_server () -> None:
    server = FastAPI()
    server.include_router(
        router=BackendV1(),
        prefix="/api/v1",
    )
    return server