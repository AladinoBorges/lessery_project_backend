from sqlalchemy.orm import Session

from src.models.user import UserModel
from src.schemas.UserBase import (
    UserCreateHashedSchema,
    UserCreateSchema,
    UserReadSchema,
    UserUpdateSchema,
)


class UsersModel:
    def create(
        user_data: UserCreateHashedSchema, database: Session
    ) -> UserReadSchema:
        new_user: UserCreateHashedSchema = UserModel(
            name=user_data.name,
            last_name=user_data.last_name,
            email=user_data.email,
            password=user_data.password,
        )

        database.add(new_user)
        database.flush()
        database.commit()
        database.refresh(new_user)

        return new_user

    def find_all(
        skip: int, limit: int, database: Session
    ) -> list[UserReadSchema]:
        users: list[UserReadSchema] = (
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

    def update(
        user_id: int, data: UserUpdateSchema, database: Session
    ) -> UserReadSchema:
        user: UserReadSchema = (
            database.query(UserModel).filter(UserModel.id == user_id).first()
        )

        if not user:
            return None
        else:
            update_data = data.dict(exclude_unset=True)

            for key, value in update_data.items():
                setattr(user, key, value)

            database.commit()
            database.refresh(user)

        return user
