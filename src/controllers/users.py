from sqlalchemy import BigInteger
from sqlalchemy.orm import Session

from src.models.user import UserModel
from src.schemas.UserBase import UserCreateSchema, UserReadSchema

"""
    write an util that receives as parameter a unencrypted password and
    returns an encrypted (hashed) string.
"""

# TODO: UTILS START


def generate_hashed_password(
    password: str, encryption_algorithm: str = "SHA256"
) -> str | None:
    return None


# TODO: UTILS END


# ! Create
def create_user(database: Session, user: UserCreateSchema) -> UserReadSchema:
    hashed_password: str = user.password
    new_user: UserReadSchema = UserModel(
        email=user.email, hashed_password=hashed_password
    )

    database.add(new_user)
    database.commit()
    database.refresh(new_user)

    return new_user


# ! Read
def get_user(database: Session, user_id: BigInteger) -> UserReadSchema:
    query_result: UserReadSchema = (
        database.query(UserModel).filter(UserModel.id == user_id).first()
    )

    return query_result


def get_user_by_email(database: Session, user_email: str) -> UserReadSchema:
    query_result: UserReadSchema = (
        database.query(UserModel).filter(UserModel.email == user_email).first()
    )

    return query_result


def get_users(
    database: Session, skip: int = 0, limit: int = 30
) -> list[UserReadSchema]:
    query_result: list[UserReadSchema] = (
        database.query(UserModel).offset(skip).limit(limit).all()
    )

    return query_result


# ! Update

# ! Delete
