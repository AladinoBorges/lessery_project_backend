from sqlalchemy.orm import Session

from src.models.product import ProductModel
from src.schemas.ProductBase import ProductCreateSchema, ProductReadSchema


class ProductsModel:
    def create(
        product: ProductCreateSchema, user_id: int, database: Session
    ) -> ProductReadSchema:
        new_product: ProductReadSchema = ProductModel(
            **product.dict(), owner_id=user_id
        )

        database.add(new_product)
        database.commit()
        database.refresh(new_product)

        return new_product

    def find_all(
        skip: int, limit: int, database: Session
    ) -> list[ProductReadSchema]:
        products: list[ProductReadSchema] = (
            database.query(ProductModel).offset(skip).limit(limit).all()
        )

        return products

    def find_by_id(product_id: int, database: Session) -> ProductReadSchema:
        product: ProductReadSchema = (
            database.query(ProductModel)
            .filter(ProductModel.id == product_id)
            .first()
        )

        return product

    def find_by_code(
        product_code: str, database: Session
    ) -> ProductReadSchema:
        product: ProductReadSchema = (
            database.query(ProductModel)
            .filter(ProductModel.code == product_code)
            .first()
        )

        return product

    def find_by_name(
        product_name: str, database: Session
    ) -> list[ProductReadSchema]:

        print("name hello")

    def find_by_category(product_category: str) -> list[ProductReadSchema]:
        # database: Session = database_connection()

        print("category hello")

    def find_by_owner_id(
        owner_id: int, database: Session
    ) -> list[ProductReadSchema]:

        product: ProductReadSchema = (
            database.query(ProductModel)
            .filter(ProductModel.owner_id == owner_id)
            .all()
        )

        return product
