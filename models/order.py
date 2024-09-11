from configs.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True, index=True)
    day = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    total_cost = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False)
    user = relationship("User", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")