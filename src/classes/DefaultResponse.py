class DefaultResponse:
    def __init__(
        self,
        status: int,
        message: str,
        environment: str,
        testing: bool,
        data: any = None,
    ) -> dict[str, int | bool | str | None | dict | list]:
        self.success = {
            "status": status,
            "error": False,
            "message": message,
            "data": data,
            "environment": environment,
            "testing": testing,
        }
