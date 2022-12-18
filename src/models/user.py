from sqlalchemy import BigInteger, Boolean, Column, String

from src.models.base import Base

""" from sqlalchemy.orm import relationship """


class UserModel(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    is_active = Column(Boolean, default=True)

    name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(32), nullable=False)

    """ login_log = Column(ARRAY(Date), nullable=True, index=True)
    logout_log = Column(ARRAY(Date), nullable=True, index=True) """

    """ products = relationship("Products", back_populates="owner") """
