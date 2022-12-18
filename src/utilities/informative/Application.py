import os

from pydantic import BaseSettings


class ApplicationInformation(BaseSettings):
    version: str = os.getenv("APP_VERSION")
    name: str = os.getenv("APP_NAME")
    testing: bool = os.getenv("TESTING")
    environment: str = os.getenv("ENVIRONMENT")
    engineers: list[dict[str, str | list[str]]] = [
        {"version": "1.0.0", "names": ["@aladinoborges"]}
    ]
