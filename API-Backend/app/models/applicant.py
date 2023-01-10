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
    id: Optional[int]
    firstname: str
    lastname: str 
    class Config:
        orm_mode = True


class ApplicantReadModel(BaseModel):

    id: Optional[int]
    username: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    password: Optional[str]
    class Config:
        orm_mode = True


class ApplicantSearchModel(BaseModel):
    id: Optional[int]
    username: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    
    class Config:
        orm_mode = True
