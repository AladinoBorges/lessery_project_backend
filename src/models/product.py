from sqlalchemy import ARRAY, BigInteger, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from src.connections.engine import Base


class ProductModel(Base):
    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)

    code = Column(String(200), nullable=False, index=True)
    name = Column(String(400), nullable=False, index=True)
    description = Column(String(2000), nullable=False, index=True)
    owner_id = Column(BigInteger, ForeignKey("users.id"))
    prices = Column(ARRAY(BigInteger), nullable=True, index=True)

    owner = relationship("User", back_populates="products")
