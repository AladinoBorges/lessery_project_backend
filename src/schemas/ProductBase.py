from pydantic import BaseModel as BaseSchema
from sqlalchemy import BigInteger


class ProductBaseSchema(BaseSchema):
    code: str
    name: str
    description: str
    owner_id: BigInteger
    prices: list[float]


class ProductCreateSchema(ProductBaseSchema):
    pass


class ProductReadSchema(ProductBaseSchema):
    id: BigInteger
    owner_id: BigInteger

    class Config:
        orm_mode: bool = True
