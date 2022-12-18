from sqlalchemy import ARRAY, BigInteger, Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from src.models.base import Base


class ProductModel(Base):
    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)

    code = Column(String(200), nullable=False, index=True)
    name = Column(String(600), nullable=False, index=True)
    price = Column(Float, nullable=False, index=True)
    description = Column(String(2000), nullable=False, index=True)
    owner_id = Column(BigInteger, ForeignKey("users.id"))
    price_history = Column(ARRAY(Float), nullable=True, index=True)
    shop_name = Column(String(80), nullable=False, index=True)
    affiliate_url = Column(String(1000), nullable=False, index=True)

    owner = relationship("User", back_populates="products")
