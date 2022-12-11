import logging
from functools import lru_cache

from pydantic import BaseSettings

from src.classes.SettingsClass import SettingsClass

log = logging.getLogger("uvicorn")


@lru_cache
def get_settings() -> BaseSettings:
    log.info("Loading config settings from environment ...")

    return SettingsClass()
