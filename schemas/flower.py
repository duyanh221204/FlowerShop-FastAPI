from pydantic import BaseModel, Field


class FlowerSchema(BaseModel):
    id: int
    name: str
    price: int
    quantity: int
    description: str


class FlowerCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    price: int = Field(gt=0)
    quantity: int = Field(gt=0)
    description: str = Field(min_length=5, max_length=10000)