from sqlalchemy import BigInteger
from sqlalchemy.orm import Session

from src.models.product import ProductModel
from src.schemas.ProductBase import (
    ProductBaseSchema,
    ProductCreateSchema,
    ProductReadSchema,
)

"""
    write an util that receives as parameter a product url (ex: amazon) and
    parses the unique id (removes all information from the url and leaves only
    the unique id).

    then, write another util that connects with amazon API and retrieves all
    necessary information for product creation on LESSERY database.
"""

# TODO: UTILS START


def get_product_unique_id(url: str) -> str | None:
    return None


def get_product_info_from_external_website(
    product_id: str,
) -> ProductBaseSchema | None:
    return None


# ? UTILS END


# ! Create
def create_product(
    database: Session, product: ProductCreateSchema, user_id: BigInteger
) -> ProductReadSchema:
    new_product: ProductReadSchema = ProductModel(
        **product.dict(), owner_id=user_id
    )

    database.add(new_product)
    database.commit()
    database.refresh(new_product)

    return new_product


# ! Read
def get_product(
    database: Session, product_id: BigInteger
) -> ProductReadSchema:
    query_result: ProductReadSchema = (
        database.query(ProductModel)
        .filter(ProductModel.id == product_id)
        .first()
    )

    return query_result


def get_product_by_code(
    database: Session, product_code: str
) -> ProductReadSchema:
    query_result: ProductReadSchema = (
        database.query(ProductModel)
        .filter(ProductModel.code == product_code)
        .first()
    )

    return query_result


def get_products(
    database: Session, skip: int = 0, limit: int = 30
) -> list[ProductReadSchema]:
    query_result: list[ProductReadSchema] = (
        database.query(ProductModel).offset(skip).limit(limit).all()
    )

    return query_result


# ! Update

# ! Delete
