from datetime import datetime
from .user_model import User
from beanie import Document, Indexed, Link, before_event, Replace, Insert
from uuid import UUID, uuid4
from pydantic import Field, EmailStr
from typing import Optional


class Todo(Document):
    todo_id: UUID = Field(default_factory=uuid4)
    status: bool = False
    title: Indexed(str)
    description: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[User]

    def __repr__(self) -> str:
        return f"Todo {self.title}"

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Todo):
            return self.todo_id == __o.todo_id
        return False

    @before_event([Replace, Insert])
    def update_updated_at(self):
        self.updated_at = datetime.utcnow()

    class Settings:
        name = "todos"
