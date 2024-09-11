from pydantic import BaseModel, Field


class Register(BaseModel):
    username: str = Field(min_length=4, max_length=20)
    email: str = Field(min_length=11, max_length=30)
    first_name: str = Field(min_length=2)
    last_name: str = Field(min_length=2)
    password: str = Field(min_length=8, max_length=20)
    role: str = "customer"


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    id: int
    username: str
    role: str


class PasswordChange(BaseModel):
    current_password: str = Field(min_length=8, max_length=20)
    new_password: str = Field(min_length=8, max_length=20)