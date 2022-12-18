import os

from pydantic import BaseSettings


class ApplicationInformation(BaseSettings):
    version: str = os.getenv("APP_VERSION")
    name: str = os.getenv("APP_NAME")
    testing: bool = os.getenv("TESTING")
    environment: str = os.getenv("ENVIRONMENT")
    history: list[dict[str, str | list[str]]] = [
        {"version": "1.0.0", "engineers": ["@aladinoborges"]}
    ]
