from datetime import datetime
from typing import List
from pydantic import BaseModel
from .teams_schemas import TeamSchema

class CompetitionSchema(BaseModel):
    name: str
    code: str
    area_name: str
    teams: List[TeamSchema]

    
    class Config:
        orm_mode = True
