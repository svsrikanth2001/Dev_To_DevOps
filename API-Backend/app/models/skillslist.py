import datetime

from pydantic import BaseModel
from typing import Optional


class SkillsListCreateModel(BaseModel):
    id: int
    name : str
    class Config:
        orm_mode = True


class SkillsListDeleteModel(BaseModel):
    message: str
    class Config:
        orm_mode = True


class SkillsListUpdateModel(BaseModel):
    id: int
    name : str
    class Config:
        orm_mode = True


class SkillsListReadModel(BaseModel):
    id: int
    name : str
    class Config:
        orm_mode = True


class SkillsListSearchModel(BaseModel):
    id: Optional[int]
    name : Optional[str]
    class Config:
        orm_mode = True
