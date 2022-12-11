import os
from typing import Callable, Optional

import sqlalchemy
from sqlalchemy.orm import Session, sessionmaker

from src.orm.model_base import Base
from src.utils.config import database_connection_logger

__connection: Optional[Callable[[], Session]] = None


def global_initializer() -> None:
    global __connection

    if __connection:
        return

    connection_string = str(
        os.environ.get(
            "DATABASE_URL", "sqlite:///backend/db/local_database.db"
        )
    )

    database_connection_logger()

    engine = sqlalchemy.create_engine(connection_string, echo=False)
    __connection = sessionmaker(bind=engine)

    from src.models.user import User

    Base.metadata.create_all(engine)


def create_session() -> Session:
    global __connection

    if not __connection:
        raise Exception(
            "You must call the global_initializer method before using"
            + " create_session method."
        )

    session: Session = __connection()
    session.expire_on_commit = False

    return session


def get_database() -> Session:
    database = create_session()

    try:
        yield database
    finally:
        database.close()
