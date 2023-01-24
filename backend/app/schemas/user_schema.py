from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="Email of the user")
    username: str = Field(..., min_length=6, max_length=20,
                          description="Username of the user")
    password: str = Field(..., min_length=6, max_length=20,
                          description="Password of the user")


class UserOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: bool = False
