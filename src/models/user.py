from sqlalchemy import BigInteger, Boolean, Column, LargeBinary, String

from src.models.base import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    is_active = Column(Boolean, default=False)
    verified = Column(Boolean, default=False)

    name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(LargeBinary(255), nullable=False)
