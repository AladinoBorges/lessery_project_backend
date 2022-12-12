from fastapi import APIRouter, Depends

from src.classes.DefaultResponse import DefaultResponse
from src.classes.SettingsClass import SettingsClass
from src.connections.engine import LocalSession
from src.utils.config import get_settings

router = APIRouter()


def settings_data() -> SettingsClass:
    return Depends(get_settings)


def get_database():
    database = LocalSession()

    try:
        yield database
    finally:
        database.close()


@router.get("/users")
async def get_users(
    settings: SettingsClass = settings_data(), database=Depends(get_database)
):
    users = database

    response = DefaultResponse(
        200,
        "users data",
        settings.version,
        settings.environment,
        settings.testing,
        users,
    )

    return response.success
