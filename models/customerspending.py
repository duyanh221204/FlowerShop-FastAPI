from configs.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class CustomerSpending(Base):
    __tablename__ = "CustomerSpending"
    id = Column(Integer, ForeignKey("Users.id"), primary_key=True, index=True)
    total_spending = Column(Integer, nullable=False)
    user = relationship("User", back_populates="spending", uselist=False)