from pydantic import BaseModel
from typing import Optional

# Shared base class for common task fields
class TaskBase(BaseModel):
    name: str
    description: Optional[str] = None
    completed: bool

# For input when creating a new task
class TaskCreate(TaskBase):
    pass

# For response/output with an ID
class Task(TaskBase):
    id: int
