from pydantic import BaseModel
from schemas.user import UserSchema
from schemas.order import OrderResponse
from typing import List
from enum import Enum


class CustomerInfo(UserSchema):
    total_spending: int
    tier: str


class CustomerOrder(BaseModel):
    user_id: int
    username: str
    total_spending: int
    orders: List[OrderResponse]


class CustomerTier(str, Enum):
    bronze = "Bronze"
    silver = "Silver"
    gold = "Gold"
    diamond = "Diamond"