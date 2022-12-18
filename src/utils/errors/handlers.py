from fastapi import HTTPException


def http_exceptions(
    error_message: str,
    error_status_code: int = 404,
) -> HTTPException:
    raise HTTPException(status_code=error_status_code, detail=error_message)
