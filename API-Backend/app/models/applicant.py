import datetime

from pydantic import BaseModel
from typing import Optional


class ApplicantCreateModel(BaseModel):

    username: str
    password: str
    firstname: str
    lastname: str 
    class Config:
        orm_mode = True


class ApplicantDeleteModel(BaseModel):
    message: str
    class Config:
        orm_mode = True


class ApplicantUpdateModel(BaseModel):
    id: int
    password: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str] 
    class Config:
        orm_mode = True


class ApplicantReadModel(BaseModel):

    id: int
    username: str
    password: str
    firstname: str
    lastname: str 
    class Config:
        orm_mode = True


class ApplicantSearchModel(BaseModel):
    id: Optional[int]
    username: Optional[str]
    firstname: str
    lastname: str 
    class Config:
        orm_mode = True
