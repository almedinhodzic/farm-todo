from fastapi import APIRouter, HTTPException, status
from app.schemas.user_schema import UserAuth, UserOut
from app.services.user_service import UserService
import pymongo

user_router = APIRouter()


@user_router.post("/create", summary="Create a new user", response_model=UserOut)
async def create_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User with email or username already exists")
