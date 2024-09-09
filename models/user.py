from configs.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    hashed_password = Column(String(1000), nullable=False)
    role = Column(String(255), default="user", nullable=False)
    orders = relationship("Order", back_populates="user")
    spending = relationship("CustomerSpending", back_populates="user", uselist=False)