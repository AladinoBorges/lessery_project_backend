from sqlalchemy import ARRAY, BigInteger, Column, Float, ForeignKey, String
from sqlalchemy.orm import Session, relationship

from src.models.base import Base
from src.models.utils.connection import database_connection
from src.schemas.ProductBase import ProductCreateSchema, ProductReadSchema


class ProductModel(Base):
    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)

    code = Column(String(200), nullable=False, index=True)
    name = Column(String(600), nullable=False, index=True)
    price = Column(Float, nullable=False, index=True)
    description = Column(String(2000), nullable=False, index=True)
    owner_id = Column(BigInteger, ForeignKey("users.id"))
    price_history = Column(ARRAY(BigInteger), nullable=True, index=True)
    shop_name = Column(String(80), nullable=False, index=True)
    affiliate_url = Column(String(1000), nullable=False, index=True)

    owner = relationship("User", back_populates="products")


class ProductsModel:
    def create(
        product: ProductCreateSchema, user_id: BigInteger
    ) -> ProductReadSchema:
        database: Session = database_connection()

        new_product: ProductReadSchema = ProductModel(
            **product.dict(), owner_id=user_id
        )

        database.add(new_product)
        database.commit()
        database.refresh(new_product)

        return new_product

    def find_all(skip: int, limit: int) -> list[ProductReadSchema]:
        database: Session = database_connection()

        products: list[ProductReadSchema] = (
            database.query(ProductModel).offset(skip).limit(limit).all()
        )

        return products

    def find_by_id(product_id: BigInteger) -> ProductReadSchema:
        database: Session = database_connection()

        product: ProductReadSchema = (
            database.query(ProductModel)
            .filter(ProductModel.id == product_id)
            .first()
        )

        return product

    def find_by_code(product_code: str) -> ProductReadSchema:
        database: Session = database_connection()

        product: ProductReadSchema = (
            database.query(ProductModel)
            .filter(ProductModel.code == product_code)
            .first()
        )

        return product

    def find_by_name(product_name: str) -> list[ProductReadSchema]:
        # database: Session = database_connection()

        print("name hello")

    def find_by_category(product_category: str) -> list[ProductReadSchema]:
        # database: Session = database_connection()

        print("category hello")

    def find_by_owner_id(owner_id: BigInteger) -> list[ProductReadSchema]:
        database: Session = database_connection()

        product: ProductReadSchema = (
            database.query(ProductModel)
            .filter(ProductModel.owner_id == owner_id)
            .all()
        )

        return product
