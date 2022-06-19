from pydantic import BaseModel
from pydantic.types import Optional
from uuid import UUID

class AuthReadModel(BaseModel):
    username: str
    password: str 
    class Config:
        orm_mode = True

class AuthResponseModel(BaseModel):
    access_token: str
    
    class Config:
        orm_mode = True