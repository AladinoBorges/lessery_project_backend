from fastapi import FastAPI

from src.api.status import status_router
from src.api.users import users_router
from src.connections.engine import engine
from src.models.base import Base
from src.utils.configurations.logging import shutdown_event, startup_event


def create_application() -> FastAPI:
    Base.metadata.create_all(bind=engine)

    application = FastAPI()
    application.include_router(users_router)
    application.include_router(status_router)

    return application


app: FastAPI = create_application()


@app.on_event("startup")
def generate_startup_log() -> None:
    startup_event()


@app.on_event("shutdown")
def generate_shutdown_log() -> None:
    shutdown_event()
