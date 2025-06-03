from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str

class TaskBase(BaseModel):
    title: str
    status: Optional[str] = "pending"
    user_id: int

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int

    class Config:
        from_attributes = True  # Required for ORM conversion in response
