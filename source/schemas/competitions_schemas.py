from datetime import datetime
from typing import List
from pydantic import BaseModel


class CompetitionSchema(BaseModel):
    name: str
    code: str
    area_name: str
    
    class Config:
        orm_mode = True
