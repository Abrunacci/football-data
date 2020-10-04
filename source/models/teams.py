from sqlalchemy import Column, String
from .base import BaseDBModel

class TeamModel(BaseDBModel):
    __tablename__ = "teams"
    name = Column(String, nullable=False)
    tla = Column(String, nullable=False)
    area_name = Column(String, nullable=False)
    email = Column(String)