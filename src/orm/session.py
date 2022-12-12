import os

from sqlalchemy import create_engine

from src.orm.model_base import Base
from src.utils.config import database_connection_logger


def global_initializer() -> None:
    # database info
    USER = os.environ.get("SQL_USER")
    PASSWORD = os.environ.get("SQL_PASSWORD")
    NAME = os.environ.get("SQL_DATABASE")
    PORT = os.environ.get("SQL_PORT")
    HOST = os.environ.get("SQL_HOST")

    connection_url = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"

    database_connection_logger()

    engine = create_engine(connection_url, echo=True)

    if not engine:
        raise Exception("Engine initialization failed.")

    Base.metadata.create_all(engine)

    try:
        yield engine

    finally:
        engine.close()
