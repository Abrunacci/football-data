from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from .teams_schemas import TeamSchema

class CompetitionSchema(BaseModel):
    name: str
    code: str
    area_name: str
    teams: List[TeamSchema] = None

    
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
