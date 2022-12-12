from datetime import date

from sqlalchemy import ARRAY, BigInteger, Column, Date, String

from src.orm.model_base import Base


class User(Base):
    __tablename__ = "users"

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    name: str = Column(String(30), nullable=False)
    last_name: str = Column(String(30), nullable=False)
    email: str = Column(String(200), nullable=False, unique=True)
    password: str = Column(String(32), nullable=False)
    created_at: date = Column(Date, nullable=False, index=True)
    updated_at: date = Column(Date, nullable=False, index=True)
    login_log: list[date] = Column(ARRAY(Date), nullable=True, index=True)
    logout_log: list[date] = Column(ARRAY(Date), nullable=True, index=True)
