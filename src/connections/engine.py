import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from src.utils.config import database_connection_logger

# database info
USER: str = os.environ.get("SQL_USER")
PASSWORD: str = os.environ.get("SQL_PASSWORD")
NAME: str = os.environ.get("SQL_DATABASE")
PORT: str = os.environ.get("SQL_PORT")
HOST: str = os.environ.get("SQL_HOST")
DATABASE_URL: str = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"

database_connection_logger()

engine = create_engine(DATABASE_URL, echo=False)

if not engine:
    raise Exception("[LESSERY] - Engine initialization failed.")

LocalSession: Session = sessionmaker(
    autocommit=False, autoflush=True, bind=engine
)

Base = declarative_base()
