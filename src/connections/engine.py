import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

# database info
# ! instalar o dotenv para lidar com as envs:
"""
    https://pypi.org/project/python-dotenv

    https://stackoverflow.com/questions/41546883/what-is-the-use-of-python-dotenv
"""
USER: str = os.environ.get("SQL_USER")
PASSWORD: str = os.environ.get("SQL_PASSWORD")
NAME: str = os.environ.get("SQL_DATABASE")
PORT: str = os.environ.get("SQL_PORT")
HOST: str = os.environ.get("SQL_HOST")
DATABASE_URL: str = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"

engine = create_engine(DATABASE_URL, echo=False)

if not engine:
    raise Exception("[LESSERY] - Engine initialization failed.")

LocalSession: Session = sessionmaker(
    autocommit=False, autoflush=True, bind=engine
)
