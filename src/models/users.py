from sqlalchemy.orm import Session

from src.models.user import UserModel
from src.schemas.UserBase import UserCreateSchema, UserReadSchema


class UsersModel:
    def create(user_data, database: Session) -> UserCreateSchema:
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

    def find_all(
        skip: int, limit: int, database: Session
    ) -> list[UserReadSchema]:
        users: UserReadSchema = (
            database.query(UserModel).offset(skip).limit(limit).all()
        )

        return users

    def find_by_id(user_id: int, database: Session) -> UserCreateSchema:
        user: UserReadSchema = (
            database.query(UserModel).filter(UserModel.id == user_id).first()
        )

        return user

    def find_by_email(user_email: str, database: Session) -> UserCreateSchema:
        user: UserReadSchema = (
            database.query(UserModel)
            .filter(UserModel.email == user_email)
            .first()
        )

        return user

    """
    def update(
        user_id: int, data: UserUpdateSchema
    ) -> UserCreateSchema:

    def delete(user_id: int, is_active: bool):
    """
