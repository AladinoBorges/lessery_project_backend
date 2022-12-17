from fastapi import Depends
from sqlalchemy.orm import Session

from src.utils.connectors.database import connect_to_database


def database_connection() -> Session:
    return Depends(connect_to_database)
