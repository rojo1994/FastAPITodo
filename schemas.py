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

class UserBase(BaseModel):
    username: str

class UserPost(UserBase):
    password: str

class UserGet(UserBase):
    id: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str