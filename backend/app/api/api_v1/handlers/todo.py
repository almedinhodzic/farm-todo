from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from app.schemas.todo_schema import TodoOut, TodoCreate, TodoUpdate
from app.deps.user_deps import get_current_user
from app.models.user_model import User
from app.services.todo_service import TodoService
from app.models.todo_model import Todo

todo_router = APIRouter()


@todo_router.get("/", summary="Get all todos of the user", response_model=List[TodoOut])
async def list(current_user: User = Depends(get_current_user)):
    return await TodoService.list_todos(current_user)


@todo_router.post("/create", summary="Create Todo", response_model=Todo)
async def create_todo(data: TodoCreate, current_user: User = Depends(get_current_user)):
    return await TodoService.create_todo(data, current_user)


@todo_router.get("/{todo_id}", summary="Get todo by todo id", response_model=TodoOut)
async def retrieve(todo_id: UUID, current_user: User = Depends(get_current_user)):
    return await TodoService.retrieve(todo_id, current_user)


@todo_router.put("/{todo_id}", summary="Update todo", response_model=TodoOut)
async def update_todo(todo_id: UUID, todo: TodoUpdate, current_user: User = Depends(get_current_user)):
    """Update Todo"""
    todo = await TodoService.update_todo(current_user, todo_id, todo)
    return todo


@todo_router.delete("/{todo_id}", summary="Delete todo")
async def delete_todo(todo_id: UUID, current_user: User = Depends(get_current_user)):
    await TodoService.delete_todo(current_user, todo_id)
