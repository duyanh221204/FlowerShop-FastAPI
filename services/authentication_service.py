from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from configs.authentication import verify_password, hash_password, create_access_token
from exceptions import raise_error
from schemas.base_response import BaseResponse
from schemas.user import UserSchema
from schemas.authentication import Register, Token, PasswordChange
from models.user import User
from services.normalize_name import normalize_name
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


def register_user(data: Register, db: Session) -> UserSchema | BaseResponse:
    user_model = User(
        username=data.username,
        email=data.email,
        first_name=normalize_name(data.first_name),
        last_name=normalize_name(data.last_name),
        hashed_password=hash_password(data.password),
        role=data.role
    )
    existing_user = db.query(User).filter(User.username == user_model.username).first()
    if existing_user:
        return raise_error(100003)
    existing_user = db.query(User).filter(User.email == user_model.email).first()
    if existing_user:
        return raise_error(100004)
    db.add(user_model)
    db.commit()
    return UserSchema(
        id=user_model.id,
        username=user_model.username,
        email=user_model.email,
        first_name=user_model.first_name,
        last_name=user_model.last_name,
        role=user_model.role
    )


def authenticate_user(form_data: OAuth2PasswordRequestForm, db: Session) -> Token | HTTPException:
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Cannot validate user!"
        )
    access_token = create_access_token(
        {"sub": user.username, "id": user.id, "role": user.role},
        timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    )
    return Token(access_token=access_token)


def change_password(password: PasswordChange, db: Session, user: dict) -> BaseResponse:
    user_model = db.query(User).filter(User.id == user.get("id")).first()
    if not verify_password(password.current_password, user_model.hashed_password):
        return raise_error(100006)
    user_model.hashed_password = hash_password(password.new_password)
    db.add(user_model)
    db.commit()
    return BaseResponse(message="Password updated!")