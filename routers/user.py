from fastapi import APIRouter, Depends
from configs.authentication import get_current_user
from configs.database import get_db
from exceptions import raise_error
from services.authentication_service import change_password
from schemas.authentication import PasswordChange

router = APIRouter(
    prefix="/api/user",
    tags=["User"]
)


@router.put("/update-password")
async def update_password(password: PasswordChange, db=Depends(get_db), user=Depends(get_current_user)):
    try:
        if user is None:
            return raise_error(100002)
        return change_password(password, db, user)
    except Exception:
        return raise_error(100007)