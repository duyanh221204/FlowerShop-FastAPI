from configs.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Flower(Base):
    __tablename__ = "Flowers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    description = Column(String(10000), nullable=False)
    order_details = relationship("OrderDetail", back_populates="flower", cascade="all, delete-orphan")