from pydantic import BaseModel


class BaseResponse(BaseModel):
    status: str = "success"
    message: str