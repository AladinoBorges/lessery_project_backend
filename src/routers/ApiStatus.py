from fastapi import APIRouter, Depends

from src.utilities.informative.Application import ApplicationInformation
from src.utilities.logs.handlers import get_settings


class ApiStatus:
    router = APIRouter(tags=["API Status"], prefix="/api/v1/status")

    @router.get("/")
    def status(
        defaultInfos: ApplicationInformation = Depends(get_settings),
    ) -> dict[str, int | bool | str | None | dict | list]:
        return {
            "status": {
                "code": 200,
                "message": "did i ear a ping? Ping, pang ping, pong!",
            },
            "application": {
                "version": defaultInfos.version,
                "name": defaultInfos.name,
                "environment": defaultInfos.environment,
                "testing": defaultInfos.testing,
            },
            "engineers": defaultInfos.engineers,
        }
