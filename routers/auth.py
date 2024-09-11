from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from configs.database import get_db
from schemas.authentication import Register
from exceptions import raise_error
from services.authentication_service import register_user, authenticate_user

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


@router.post("/create-user")
async def create_user(data: Register, db=Depends(get_db)):
    try:
        return register_user(data, db)
    except Exception:
        return raise_error(100005)


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    return authenticate_user(form_data, db)