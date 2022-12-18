def response(
    data,
    error_message: str,
    error_status_code: int,
    success_status_code: int = 200,
):
    if data is None:
        return {
            "error": True,
            "status_code": error_status_code,
            "message": error_message,
        }

    return {"success": True, "status_code": success_status_code, "data": data}
