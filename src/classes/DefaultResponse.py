class DefaultResponse:
    def __init__(
        self,
        status: int,
        message: str,
        app_version: str,
        environment: str,
        testing: bool,
        data: any = None,
    ) -> dict[str, int | bool | str | None | dict | list]:
        self.success = {
            "status": {"code": status, "error": False, "message": message},
            "data": data,
            "api_info": {
                "version": app_version,
                "environment": environment,
                "testing": testing,
                "developers": ["@aladinoborges"],
            },
        }
