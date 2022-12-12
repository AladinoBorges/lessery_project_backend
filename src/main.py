from fastapi import FastAPI

from src.api import status
from src.orm.session import global_initializer
from src.utils.config import shutdown_event, startup_event


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(status.router, tags=["Hello"], prefix="/api/v1")

    return application


app: FastAPI = create_application()


@app.on_event("startup")
async def generate_startup_log() -> None:
    startup_event()

    global_initializer()


@app.on_event("shutdown")
async def generate_shutdown_log() -> None:
    shutdown_event()
