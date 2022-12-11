import logging
from functools import lru_cache

from pydantic import BaseSettings

from src.classes.SettingsClass import SettingsClass

log: logging.Logger = logging.getLogger("uvicorn")


def startup_event() -> None:
    log.info("[LESSERY] - Starting up the application ...")


def shutdown_event() -> None:
    log.info("[LESSERY] - Closing the application ...")


@lru_cache
def get_settings() -> BaseSettings:
    log.info("[LESSERY] - Loading config settings from environment ...")

    return SettingsClass()
