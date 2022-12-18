class Default:
    def unique(data, error_message: str, error_status_code: int):
        if data is None:
            return {
                "error": True,
                "status_code": error_status_code,
                "message": error_message,
            }

        return data

    def multiple(data, error_message: str, error_status_code: int):
        if len(data) == 0:
            return {
                "error": True,
                "status_code": error_status_code,
                "message": error_message,
            }

        return data
