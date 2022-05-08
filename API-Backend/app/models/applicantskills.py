import datetime

from pydantic import BaseModel
from typing import Optional


class ApplicantSkillsCreateModel(BaseModel):
    id: int
    applicant_login_id : int
    skillid : int
    class Config:
        orm_mode = True


class ApplicantSkillsDeleteModel(BaseModel):
    message: str
    class Config:
        orm_mode = True


class ApplicantSkillsUpdateModel(BaseModel):
    id: int
    applicant_login_id : int
    skillid : int
    class Config:
        orm_mode = True


class ApplicantSkillsReadModel(BaseModel):
    id: int
    applicant_login_id : int
    skillid : int
    class Config:
        orm_mode = True


class ApplicantSkillsSearchModel(BaseModel):
    id: Optional[int]
    applicant_login_id : Optional[int]
    skillid : Optional[int]
    class Config:
        orm_mode = True
