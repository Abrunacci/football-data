from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import BaseDBModel

class TeamModel(BaseDBModel):
    __tablename__ = "teams"
    name = Column(String, nullable=False)
    tla = Column(String, nullable=False)
    area_name = Column(String, nullable=False)
    email = Column(String)
    competitions = relationship('CompetitionModel', secondary='competitions_teams')
    players = relationship('PlayerModel', secondary='teams_players')