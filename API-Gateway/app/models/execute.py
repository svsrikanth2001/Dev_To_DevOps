from pydantic import BaseModel, Json
from typing import Optional


class ExecutePostModel(BaseModel):

    service: str
    path: str
    method: str
    query: Optional[str]
    data: Optional[dict] = {}


class ExecutePostResponseModel(BaseModel):

    data: Optional[Json]
    message: Optional[str]
    status_code: int