from datetime import datetime
from typing import List
from pydantic import BaseModel

from .players_schemas import PlayerSchema

class TeamSchema(BaseModel):
    name: str
    tla: str
    area_name: str
    email: str
    players: List[PlayerSchema] = None

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
