from fastapi import APIRouter, Depends

from src.classes.DefaultResponse import DefaultResponse
from src.classes.SettingsClass import SettingsClass
from src.utils.config import get_settings

router = APIRouter()


def settings_data() -> SettingsClass:
    return Depends(get_settings)


@router.get("/status")
async def ping(
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


@router.get("*")
async def not_found(
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
