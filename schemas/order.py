from pydantic import BaseModel
from typing import List


class OrderDetailCreate(BaseModel):
    flower_id: int
    quantity: int


class OrderCreate(BaseModel):
    order_details: List[OrderDetailCreate]


class OrderDetailResponse(BaseModel):
    id: int
    flower_id: int
    quantity: int
    total_price: int


class OrderResponse(BaseModel):
    id: int
    total_cost: int
    day: int
    month: int
    year: int
    order_details: List[OrderDetailResponse]