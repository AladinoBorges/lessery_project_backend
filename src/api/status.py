from fastapi import APIRouter, Depends

from src.classes.DefaultResponse import DefaultResponse
from src.classes.SettingsClass import SettingsClass
from src.utils.configurations.logging import get_settings

status_router = APIRouter(tags=["API Status"], prefix="/api/v1/status")


def settings_data() -> SettingsClass:
    return Depends(get_settings)


@status_router.get("/")
def ping(
    settings: SettingsClass = settings_data(),
) -> dict[str, int | bool | str | None | dict | list]:
    response = DefaultResponse(
        200,
        "pong.",
        settings.version,
        settings.environment,
        settings.testing,
    )

    return response.success


@status_router.get("/{*}")
def not_found(
    settings: SettingsClass = settings_data(),
) -> dict[str, int | bool | str | None | dict | list]:
    response = DefaultResponse(
        404,
        "ups! i did it again, 404.",
        settings.version,
        settings.environment,
        settings.testing,
    )

    return response.success
