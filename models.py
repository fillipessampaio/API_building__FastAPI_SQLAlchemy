from sqlalchemy import Column, Integer, String, Float

from database import Base


class VendasModel(Base):
    __tablename__ = "vendas"

    id: int = Column(Integer, primary_key=True, index=True)
    product: str = Column(String(100), nullable=False)
    id_seller: int = Column(Integer, nullable=False)
    price: float = Column(Float, nullable=False)
