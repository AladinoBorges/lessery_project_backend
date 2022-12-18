from datetime import date

from pydantic import BaseModel as BaseSchema

from src.schemas.ProductBase import Product


class UserBaseSchema(BaseSchema):
    name: str
    last_name: str
    email: str


class UserCreateSchema(UserBaseSchema):
    password: str


class User(UserBaseSchema):
    id: int
    is_active: bool
    products: list[Product] = []

    login_log: list[date] = []
    logout_log: list[date] = []

    class Config:
        orm_mode: bool = True


class UserReadSchema(BaseSchema):
    success: bool
    status_code: int
    data: User


class UsersReadSchema(BaseSchema):
    success: bool
    status_code: int
    data: list[User]
