from src.utilities.errors.handlers import Exceptions


class Default:
    def unique(data, message: str, code: int):
        if data is None:
            return Exceptions.http(message, code)

        return data

    def multiple(data, message: str, code: int):
        if len(data) == 0:
            return Exceptions.http(message, code)

        return data
