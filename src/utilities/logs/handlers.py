import logging
from functools import lru_cache

from pydantic import BaseSettings

from src.utilities.informative.Application import ApplicationInformation

log: logging.Logger = logging.getLogger("uvicorn")


class LogsHandlers:
    def startup() -> None:
        log.info("[LESSERY] - Starting up the application ...")

    def shutdown() -> None:
        log.info("[LESSERY] - Closing the application ...")

    def database_connection() -> None:
        log.info("[LESSERY] - Connecting to database ...")

    @lru_cache
    def get_settings() -> BaseSettings:
        log.info("[LESSERY] - Loading config settings from environment ...")

        return ApplicationInformation()
