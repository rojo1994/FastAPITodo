from pydantic import BaseModel
from typing import Optional

class taskBase(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False

class taskPost(taskBase):
    pass

class taskGet(taskBase):
    id: int

    class Config:
        from_attributes = True