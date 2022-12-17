from src.connections.engine import LocalSession


def connect_to_database() -> None:
    """get_database starts and finishes a session per request. no session
    will be used on more than one request."""
    database = LocalSession()

    try:
        yield database
    finally:
        database.close()
