from datetime import date

from pydantic import BaseModel as BaseSchema
from sqlalchemy import BigInteger

from src.schemas.ProductBase import Product


class UserBaseSchema(BaseSchema):
    name: str
    last_name: str
    email: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserReadSchema(UserBaseSchema):
    id: BigInteger
    is_active: bool
    products: list[Product] = []

    login_log: list[date] = []
    logout_log: list[date] = []

    class Config:
        orm_mode: bool = True
