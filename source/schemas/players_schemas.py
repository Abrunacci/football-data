from datetime import datetime
from typing import List
from pydantic import BaseModel


class PlayerSchema(BaseModel):
    name: str
    position: str
    day_of_birth: datetime
    country_of_birth: str
    nationality: str

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
