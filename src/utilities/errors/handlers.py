from fastapi import HTTPException


class Exceptions:
    def http(message: str, code: int) -> HTTPException:
        raise HTTPException(status_code=code, detail=message)
