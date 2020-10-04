from sqlalchemy import (Column, 
                        String, 
                        DateTime, 
                        ForeignKey,
                        Integer)
from .base import BaseDBModel


class PlayerModel(BaseDBModel):
    __tablename__ = 'players'
    name = Column(String, nullable=False)
    day_of_birth = Column(DateTime)
    position = Column(String)
    country_of_birth = Column(String)
    nationality = Column(String)
    team = Column(Integer, ForeignKey('teams.id'))