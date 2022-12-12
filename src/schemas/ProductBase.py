from pydantic import BaseModel as BaseSchema
from sqlalchemy import BigInteger


class ProductBaseSchema(BaseSchema):
    code: str
    name: str
    description: str
    price: float


class ProductCreateSchema(ProductBaseSchema):
    owner_id: BigInteger


class ProductReadSchema(ProductBaseSchema):
    id: BigInteger
    owner_id: BigInteger
    price_history: list[float]

    class Config:
        orm_mode: bool = True
