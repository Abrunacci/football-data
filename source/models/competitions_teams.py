from sqlalchemy import (Column, 
                        ForeignKey,
                        Integer,
                        PrimaryKeyConstraint)
from sqlalchemy.orm import relationship
from .base import Base

class CompetitionTeamModel(Base):
    __tablename__ = 'competitions_teams'
    __table_args__ = (
        PrimaryKeyConstraint('competition_id', 'team_id'),
    )
    competition_id = Column(Integer, ForeignKey('competitions.id'))
    team_id = Column(Integer, ForeignKey('teams.id'))
