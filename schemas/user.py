from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    role: str