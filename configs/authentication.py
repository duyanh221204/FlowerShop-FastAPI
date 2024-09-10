from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
from schemas.authentication import TokenData
from typing import Annotated
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/api/auth/token")


def verify_password(password, hashed_password):
    return bcrypt_context.verify(password, hashed_password)


def hash_password(password):
    return bcrypt_context.hash(password)


def create_access_token(data: dict, expired_delta: timedelta):
    to_encode = data.copy()
    expires = datetime.now(timezone.utc) + expired_delta
    to_encode.update({"exp": expires})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int = payload.get("id")
        username: str = payload.get("username")
        role: str = payload.get("role")
        if id is None or username is None or role is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Cannot validate user!"
            )
        return TokenData(
            id=id,
            username=username,
            role=role
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot validate user!"
        )