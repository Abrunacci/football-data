from sqlalchemy import (Column, 
                        ForeignKey,
                        Integer,
                        PrimaryKeyConstraint)
from .base import Base

class TeamPlayerModel(Base):
    __tablename__ = 'teams_players'
    __table_args__ = (
        PrimaryKeyConstraint('team_id', 'player_id'),
    )
    player_id = Column(Integer, ForeignKey('players.id'))
    team_id = Column(Integer, ForeignKey('teams.id'))