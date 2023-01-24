from fastapi import APIRouter
from app.api.api_v1.handlers.user import user_router
from app.api.auth.jwt import auth_router
from app.api.api_v1.handlers.todo import todo_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["Users"])
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(todo_router, prefix="/todos", tags=["Todos"])
