from configs.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class OrderDetail(Base):
    __tablename__ = "OrderDetails"
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Integer, nullable=False)
    flower_id = Column(Integer, ForeignKey("Flowers.id", ondelete="CASCADE"), nullable=False)
    order_id = Column(Integer, ForeignKey("Orders.id"), nullable=False)
    flower = relationship("Flower", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")