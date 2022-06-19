from pydantic import BaseModel
from pydantic.types import Optional
from uuid import UUID

class CreateRegistrationModel(BaseModel):
    username: str
    password: str
    firstname: str
    lastname: str
    class Config:
        orm_mode = True


class RegistrationResponseModel(BaseModel):
    id: str
    username: str
    firstname: str
    lastname: str
    class Config:
        orm_mode = True
