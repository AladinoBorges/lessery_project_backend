from sqlalchemy import ARRAY, BigInteger, Boolean, Column, Date, String
from sqlalchemy.orm import Session, relationship

from src.models.base import Base
from src.models.utils.connection import database_connection
from src.schemas.UserBase import UserCreateSchema, UserReadSchema


class UserModel(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    is_active = Column(Boolean, default=True)

    name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(32), nullable=False)

    login_log = Column(ARRAY(Date), nullable=True, index=True)
    logout_log = Column(ARRAY(Date), nullable=True, index=True)

    products = relationship("Products", back_populates="owner")


class UsersModel:
    def create(user_data) -> UserCreateSchema:
        database: Session = database_connection()

        new_user: UserReadSchema = UserModel(
            name=user_data.name,
            last_name=user_data.last_name,
            email=user_data.email,
            password=user_data.password,
        )

        database.add(new_user)
        database.commit()
        database.refresh(new_user)

        return new_user

    def find_all(skip: int, limit: int) -> list[UserReadSchema]:
        database: Session = database_connection()

        users: list[UserReadSchema] = (
            database.query(UserModel).offset(skip).limit(limit).all()
        )

        return users

    def find_by_id(user_id: BigInteger) -> UserCreateSchema:
        database: Session = database_connection()

        user: UserReadSchema = (
            database.query(UserModel).filter(UserModel.id == user_id).first()
        )

        return user

    def find_by_email(user_email: str) -> UserCreateSchema:
        database: Session = database_connection()

        user: UserReadSchema = (
            database.query(UserModel)
            .filter(UserModel.email == user_email)
            .first()
        )

        return user

    """
    def update(user_id: int, data: UserUpdateSchema) -> UserCreateSchema:
        database: Session = database_connection()

    def delete(user_id: int, is_active: bool):
        database: Session = database_connection()
    """
