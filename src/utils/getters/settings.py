from fastapi import Depends

from src.classes.SettingsClass import SettingsClass
from src.utils.configurations.logging import get_settings


def settings_data() -> SettingsClass:
    return Depends(get_settings)
