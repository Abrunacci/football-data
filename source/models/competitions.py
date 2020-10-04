from sqlalchemy import Column, String

from .base import BaseDBModel


class CompetitionModel(BaseDBModel):
    """Competitons model class representation."""
    __tablename__ = 'competitions'
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    area_name = Column(String, nullable=False)