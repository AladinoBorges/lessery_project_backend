import os

from pydantic import BaseSettings


class SettingsClass(BaseSettings):
    version: str = os.getenv("APP_VERSION", "1.0.0")
    testing: bool = os.getenv("TESTING", False)
    environment: str = os.getenv("ENVIRONMENT", "dev")
