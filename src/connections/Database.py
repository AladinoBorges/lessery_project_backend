from sqlalchemy.orm import Session

from src.connections.engine import LocalSession
from src.utilities.logs.handlers import LogsHandlers


class Database:
    def connect() -> None:
        """get_database starts and finishes a session per request. no session
        will be used on more than one request."""
        database: Session = LocalSession()

        LogsHandlers.database_connection()

        try:
            yield database
        except Exception:
            database.rollback()
        finally:
            database.close()
