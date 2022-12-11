from fastapi import Depends, FastAPI

from src.classes.DefaultResponse import DefaultResponse
from src.classes.SettingsClass import SettingsClass
from src.utils.config import get_settings

app = FastAPI()


def settings_data() -> SettingsClass:
    return Depends(get_settings)


@app.get("/")
async def home(
    settings: SettingsClass = settings_data(),
) -> dict[str, int | bool | str | None | dict | list]:
    response = DefaultResponse(
        200,
        "welcome to the homepage.",
        settings.environment,
        settings.testing,
    )

    return response.success


@app.get("/ping")
async def ping(
    settings: SettingsClass = settings_data(),
) -> dict[str, int | bool | str | None | dict | list]:
    response = DefaultResponse(
        200, "pong.", settings.environment, settings.testing
    )

    return response.success


@app.get("*")
async def not_found(
    settings: SettingsClass = settings_data(),
) -> dict[str, int | bool | str | None | dict | list]:
    response = DefaultResponse(
        404,
        "ups! i did it again, 404.",
        settings.environment,
        settings.testing,
    )

    return response.success
