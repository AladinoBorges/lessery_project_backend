from fastapi import FastAPI

from src.api import status, users
from src.connections.engine import engine
from src.models.base import Base
from src.utils.configurations.logging import (
    database_connection_logger,
    shutdown_event,
    startup_event,
)


def create_application() -> FastAPI:
    Base.metadata.create_all(engine)

    application = FastAPI()
    application.include_router(
        status.router, tags=["API Status"], prefix="/api/v1"
    )
    application.include_router(users.router, tags=["Users"], prefix="/api/v1")

    database_connection_logger()

    return application


app: FastAPI = create_application()


@app.on_event("startup")
def generate_startup_log() -> None:
    startup_event()


@app.on_event("shutdown")
def generate_shutdown_log() -> None:
    shutdown_event()
