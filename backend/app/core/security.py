from datetime import datetime, timedelta
from typing import Any, Union
from passlib.context import CryptContext
from jose import jwt

from app.core.config import settings

password_context = CryptContext(schemes=["bcrypt"])


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow(
        ) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)

    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow(
        ) + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode, settings.JTW_REFRESH_SECRET_KEY, algorithm=settings.ALGORITHM)

    return encoded_jwt


def get_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)
