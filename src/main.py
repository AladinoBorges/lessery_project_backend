from fastapi import FastAPI

from src.api.users import users_router
from src.connections.engine import engine
from src.models.base import Base
from src.routers.ApiStatus import ApiStatus
from src.utilities.logs.handlers import LogsHandlers


def create_application() -> FastAPI:
    Base.metadata.create_all(bind=engine)

    application = FastAPI()

    application.include_router(users_router)
    application.include_router(ApiStatus.router)

    return application


app: FastAPI = create_application()

""" @app.exception_handler(AppExceptionCase)
def handle_exceptions(request, error):
    return app_exception_handler(request, error) """


@app.on_event("startup")
def generate_startup_log() -> None:
    LogsHandlers.startup()


@app.on_event("shutdown")
def generate_shutdown_log() -> None:
    LogsHandlers.shutdown()
