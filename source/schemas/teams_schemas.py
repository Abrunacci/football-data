from datetime import datetime
from typing import List
from pydantic import BaseModel


class TeamSchema(BaseModel):
    name: str
    tla: str
    area_name: str
    email: str

    class Config:
        orm_mode = True
