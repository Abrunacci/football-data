from sqlalchemy import Column, String

from .base import BaseModel


class CompetitionModel(BaseModel):
    """Competitons model class representation."""
    __tablename__ = 'competitions'
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    area_name = Column(String, nullable=False)